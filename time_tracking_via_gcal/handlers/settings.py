import re
import pprint

from aiogram import types

from ..models.dal import (
    get_user_settings,
    update_user_settings,
)
from ..structs import States
from ..app import dp


edit_button = types.InlineKeyboardButton(
    "edit", callback_data="edit_settings"
)
inl_keyboard = types.InlineKeyboardMarkup().add(
    edit_button
)

# S = SETTINGS
S_REG = (
    r"(\d+|(?:\d+\.\d+)) ([A-Z]{3}) *((?:.*, ?)*.*)"
)
S_SHOW_MSG = "Your settings are:\n\n{}"

S_FMT_MSG = (
    "Enter new settings in the format like\n"
    "{hour_rate} {currency} '{tag1}','{tag2}'...'{tagX}'\n"
    "number of tags could be from 0 to any number."
    "then any value will be accepted inside []\nExamples:\n"
    "40.0 EUR GT,dev,sprint2-1-0\n"
    "40.0 EUR ,,sprint2-1-0\n"
    "1000 RUB"
)
S_WRONG_FMT_MSG = "Wrong format, please:\n\n"
S_UPD_SUCCESS_MSG = "Settings updated successfully"


async def settings_get(msg: types.Message):
    settings: str = pprint.pformat(
        await get_user_settings(msg.from_user.id),
        width=40,
        indent=0,
    ).strip(" {}")
    await msg.reply(
        S_SHOW_MSG.format(settings),
        reply_markup=inl_keyboard,
    )


async def settings_edit_callback(
    callback: types.CallbackQuery
):
    state = dp.current_state()
    await state.set_state(States.EDIT.value)
    await callback.bot.send_message(
        callback.from_user.id, text=S_FMT_MSG
    )


async def settings_set(msg: types.Message):
    try:
        rate, currency, tags = re.fullmatch(
            S_REG, msg.text
        ).groups()
        tags = tags.replace(" ", "").split(",")
    except:
        await msg.reply(S_WRONG_FMT_MSG + S_FMT_MSG)
    else:
        await update_user_settings(
            rate, currency, tags
        )
        await msg.reply(S_UPD_SUCCESS_MSG)
        await settings_get(msg)
        state = dp.current_state()
        await state.set_state(States.VIEWING.value)
