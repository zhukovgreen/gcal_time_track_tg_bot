import re


from aiogram import types

from ..structs import States
from ..app import dp
from ..models.user import UserTable


edit_button = types.InlineKeyboardButton(
    "edit", callback_data="edit_settings"
)
inl_keyboard = types.InlineKeyboardMarkup().add(
    edit_button
)


async def settings(msg: types.Message):
    engine: Engine = dp["pg"]
    async with engine.acquire() as conn:
        conn: SAConnection
        resp = await conn.execute(
            UserTable.select().where(
                UserTable.c.user_id
                == msg.from_user.id
            )
        )
        tags = await resp.fetchone()

    await msg.reply(
        f"Your serach tags are {repr(tags[1])}",
        reply_markup=inl_keyboard,
    )


async def settings_edit(
    callback: types.CallbackQuery
):
    state = dp.current_state()
    await state.set_state(States.EDIT.value)
    await callback.bot.send_message(
        callback.from_user.id,
        text=(
            "Enter new values for a search tags. "
            "Separate them with the coma `,`. "
            "For example `GT,dev,sprint2-1-0` "
        ),
    )


async def process_search_tags(msg: types.Message):
    res = re.findall(r"[\w+]+|\*+", msg.text)
    res
