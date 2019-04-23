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


from ..app import dp
from ..structs import States

logger = logging.getLogger("aiogram")


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
    await create_new_user(msg)

    await msg.reply(
        "This bot helps you track your time and generate useful reports.\n"
        "The bot uses a special system of tags in your calendar.\n"
        "If you would like to make a bot notice your event you have to have "
        "the following event name "
        "`[some_tag] [another_tag] [yet_another_tag] some text here`.\n"
        "The bot identifies tags in your calendar events and agregate "
        "the events into useful report taking in to account your settings.\n\n"
        "`\settings` - To check your settings\n"
        "`\help` - get help, submit support ticket\n"
        r"`\report` - get help, submit support ticket."
    )
    await msg.reply(
        "Main menu activated", reply_markup=main_menu
    )
    state = dp.current_state()
    await state.set_state(States.VIEWING.value)
