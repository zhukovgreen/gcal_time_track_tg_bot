from aiogram import types

from ..app import dp


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
    import ipdb

    ipdb.set_trace()
