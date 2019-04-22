import re
import pprint

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

    settings: dict = dict(
        zip(UserTable.columns.keys(), tags.as_tuple())
    )
    del settings["user_id"]
    settings: str = pprint.pformat(
        settings, width=40, indent=0
    ).strip(" {}")
    await msg.reply(
        f"Your settings are:\n{settings}",
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
            "Enter new settings in the format like\n"
            "{hour_rate} {currency} | '{tag1}', '{tag2}' ... '{tagX}'\n"
            "number of tags could be from 1 to any number. If '' given, then "
            "then any value will be accepted inside []\nExamples:\n"
            "40.0 EUR | 'GT', 'dev', 'sprint2-1-0'\n"
            "40.0 EUR | '', '', 'sprint2-1-0'\n"
            "1000 RUB | ''"
        ),
    )


async def settings_set(msg: types.Message):
    rate, currency, tags = re.findall(r"", msg.text)
