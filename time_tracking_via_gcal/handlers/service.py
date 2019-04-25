import pickle
import io
import json
import logging
from enum import Enum

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
from ..structs import States
from ..models.dal import update_user, create_new_user
from ..utils.gcal_manager import build_gcal

logger = logging.getLogger("aiogram")

INTRO_MSG = (
    "This bot helps you track your time and generate useful reports.\n"
    "The bot uses a special system of tags in your calendar.\n"
    "If you would like to make a bot notice your event you have to have "
    "the following event name "
    "`[some_tag] [another_tag] [yet_another_tag] some text here`.\n"
    "The bot identifies tags in your calendar events and agregate "
    "the events into useful report taking in to account your settings.\n\n"
    "`/settings` - To check your settings\n"
    "`/help` - get help, submit support ticket\n"
    r"`/report` - get help, submit support ticket."
)

ALREADY_REGISTRED_USER_MSG = (
    "User with this id is already registered"
)

GCAL_BUILD_NOTIF_MSG = (
    r"Google calendar was built for a user {user_id}"
)


class ReportPeriod(Enum):
    prev_month: str = "previous month"
    this_month: str = "this month"
    prev_week: str = "previous week"
    this_week: str = "this week"


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


async def echo(msg: types.Message):
    await msg.reply(msg)


async def reset_state(msg: types.Message):
    state = dp.current_state()
    await state.reset_state()
    await msg.reply(
        f"Your current state is {await state.get_state()}"
    )


async def start(msg: types.Message):
    await msg.reply(INTRO_MSG)
    try:
        await create_new_user(msg.from_user.id)
    except UniqueViolation:
        await msg.reply(ALREADY_REGISTRED_USER_MSG)

    await msg.reply("Now, enter your calendar id")
    state = dp.current_state()
    await state.set_state(States.AUTH_CAL_ID.value)


async def get_cal_id(msg: types.Message):

    try:
        await update_user(
            msg.from_user.id, cal_id=msg.text
        )
    except:
        await msg.reply("Something went wrong")
    else:
        await msg.reply(
            "OK. Now send me the json file, "
            "which you generated from google api"
        )
        state = dp.current_state()
        await state.set_state(
            States.AUTH_SECRETS.value
        )


async def get_secrets(msg: types.Message):
    secrets = await msg.document.download(
        destination=io.BytesIO()
    )
    secrets = json.loads(secrets.read().decode())
    gcal = build_gcal(secrets)
    logger.info(
        GCAL_BUILD_NOTIF_MSG.format(
            user_id=msg.from_user.id
        )
    )

    try:
        await update_user(
            msg.from_user.id,
            secrets=secrets,
            cal_service=pickle.dumps(gcal),
        )
    except:
        await msg.reply("Something went wrong")
    else:
        await msg.reply(
            "Great. Now you can use the bot",
            reply_markup=main_menu,
        )
        state = dp.current_state()
        await state.set_state(States.VIEWING.value)
