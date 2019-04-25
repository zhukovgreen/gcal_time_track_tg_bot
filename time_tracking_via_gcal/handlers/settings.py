import re
import pprint

from aiogram import types

from ..models.dal import (
    get_report_settings,
    update_report_settings,
)
from ..structs import States
from ..app import dp
from ..messages import (
    S_REG,
    S_SHOW_MSG,
    S_FMT_MSG,
    S_WRONG_FMT_MSG,
    S_UPD_SUCCESS_MSG,
)


SETTINGS_WIDTH = 40
SETTINGS_INDENT = 0
SETTINGS_STRIP = " {}"

EDIT_SETTINGS_CALLBACK_NAME = "edit_settings"


edit_button = types.InlineKeyboardButton(
    "edit", callback_data=EDIT_SETTINGS_CALLBACK_NAME
)
inl_keyboard = types.InlineKeyboardMarkup().add(
    edit_button
)


async def report_settings_get(msg: types.Message):
    settings: str = pprint.pformat(
        await get_report_settings(msg),
        width=SETTINGS_WIDTH,
        indent=SETTINGS_INDENT,
    ).strip(SETTINGS_STRIP)
    await msg.reply(
        S_SHOW_MSG.format(settings=settings),
        reply_markup=inl_keyboard,
    )


async def report_settings_edit_callback(
    callback: types.CallbackQuery
):
    state = dp.current_state()
    await state.set_state(States.EDIT.value)
    await callback.bot.send_message(
        callback.from_user.id, text=S_FMT_MSG
    )


async def report_settings_set(msg: types.Message):
    try:
        rate, currency, tags = re.fullmatch(
            S_REG, msg.text
        ).groups()
        tags = (
            tags.replace(" ", "").lower().split(",")
        )
    except:
        await msg.reply(S_WRONG_FMT_MSG +" please:\n\n" + S_FMT_MSG)
    else:
        await update_report_settings(
            msg, rate, currency, tags
        )
        await msg.reply(S_UPD_SUCCESS_MSG)
        await report_settings_get(msg)
        state = dp.current_state()
        await state.set_state(States.VIEWING.value)
