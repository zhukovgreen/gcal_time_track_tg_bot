import pickle
import io
import json
import logging

from aiogram import types
from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from psycopg2.errors import UniqueViolation


from ..app import dp
from ..structs import States, ReportPeriod
from ..models.dal import update_user, create_new_user
from .utils import build_gcal
from ..messages import (
    INTRO_MSG,
    HELP_MSG,
    ALREADY_REGISTRED_USER_MSG,
    CURRENT_STATE_MSG,
    ENTER_CAL_ID_MSG,
    SMTH_WENT_WRONG_MSG,
    SEND_JSON_MSG,
    SETTING_FMT_MSG,
    YOU_CAN_USE_BOT_MSG,
    THIS_IS_BAD_FILE_MSG,
)

logger = logging.getLogger(__name__)

SUBMIT_TICKET_URL = "https://google.com"
SUPPORT_CHAT_URL = "https://google.com"


main_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(
                ReportPeriod.prev_month.value
            ),
            KeyboardButton(
                ReportPeriod.this_month.value
            ),
        ],
        [
            KeyboardButton(
                ReportPeriod.prev_week.value
            ),
            KeyboardButton(
                ReportPeriod.this_week.value
            ),
        ],
    ],
    resize_keyboard=True,
)

help_menu = InlineKeyboardMarkup()
help_menu.add(
    InlineKeyboardButton(
        "submit ticket", url=SUBMIT_TICKET_URL
    )
)
help_menu.add(
    InlineKeyboardButton(
        "join support chat", url=SUPPORT_CHAT_URL
    )
)


async def echo(msg: types.Message):
    await msg.reply(msg)


async def reset_state(msg: types.Message):
    state = dp.current_state()
    await state.reset_state()
    await msg.reply(
        CURRENT_STATE_MSG.format(
            state=await state.get_state()
        )
    )


async def start(msg: types.Message):
    await msg.reply(INTRO_MSG)
    try:
        await create_new_user(msg.from_user.id)
    except UniqueViolation:
        await msg.reply(ALREADY_REGISTRED_USER_MSG)

    await msg.reply(ENTER_CAL_ID_MSG)
    state = dp.current_state()
    await state.set_state(States.AUTH_CAL_ID.value)


async def help_handler(msg: types.Message):
    await msg.reply(
        HELP_MSG + "\n\n" + INTRO_MSG,
        reply_markup=help_menu,
    )


async def get_cal_id(msg: types.Message):

    try:
        await update_user(
            msg.from_user.id, cal_id=msg.text
        )
    except:
        await msg.reply(SMTH_WENT_WRONG_MSG)
    else:
        await msg.reply(SEND_JSON_MSG)
        state = dp.current_state()
        await state.set_state(
            States.AUTH_SECRETS.value
        )


async def get_secrets(msg: types.Message):
    secrets = await msg.document.download(
        destination=io.BytesIO()
    )
    try:
        secrets = json.loads(secrets.read().decode())
    except json.JSONDecodeError:
        await msg.reply(THIS_IS_BAD_FILE_MSG)
    else:
        try:
            gcal = build_gcal(secrets)
            logger.info(
                r"Google calendar was built for the user {user_id}".format(
                    user_id=msg.from_user.id
                )
            )
            await update_user(
                msg.from_user.id,
                secrets=secrets,
                cal_service=pickle.dumps(gcal),
            )
        except:
            await msg.reply(SMTH_WENT_WRONG_MSG)
        else:
            await msg.reply(
                YOU_CAN_USE_BOT_MSG
                + "\n\n"
                + SETTING_FMT_MSG,
                reply_markup=main_menu,
            )
            state = dp.current_state()
            await state.set_state(States.EDIT.value)
