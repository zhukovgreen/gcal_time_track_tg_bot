from enum import Enum

from aiogram import types, Bot

from ..app import dp


class States(Enum):
    EDIT: str = "EDIT"
    VIEWING: str = "VIEWING"


edit_button = types.InlineKeyboardButton(
    "edit", callback_data="edit_settings"
)
inl_keyboard = types.InlineKeyboardMarkup().add(
    edit_button
)


async def settings(msg: types.Message):
    await msg.reply(
        f"Your settings are ...",
        reply_markup=inl_keyboard,
    )


async def settings_edit(
    callback: types.CallbackQuery
):
    state = dp.current_state(
        user=callback.from_user.id
    )
    state.set_data(States.EDIT)
    bot: Bot = callback.bot
    await bot.send_message(
        callback.from_user.id,
        text=(
            "Enter new values for a search tags. "
            "Separate tehm with the coma `,`. "
            "For example `GT,dev,sprint2-1-0`"
        )
    )
