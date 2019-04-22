from concurrent.futures import ThreadPoolExecutor
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

import pendulum
from googleapiclient.discovery import Resource
from aiopg.sa.engine import Engine
from aiopg.sa.connection import SAConnection
from sqlalchemy.sql.dml import Insert
from psycopg2 import errors

from ..app import dp
from ..structs import States
from ..gcal_manager import get_events
from .data_processing import form_report
from ..utils import rm
from ..models.user import UserTable


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
    state = dp.current_state()
    engine: Engine = dp["pg"]
    async with engine.acquire() as conn:
        conn: SAConnection

        query: Insert = UserTable.insert().values(
            user_id=msg.from_user.id,
            tags=("", ""),
            currency="",
            rate=0,
        )
        try:
            await conn.execute(query)
        except errors.UniqueViolation:
            await msg.reply(
                "User with this id is already registered"
            )
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
    await state.set_state(States.VIEWING.value)


def report_handler_factory(
    period: ReportPeriod,
    executor: ThreadPoolExecutor,
    gcal: Resource,
):
    async def report_handler(msg: types.Message):
        now = pendulum.now("UTC")
        prev_month = now.subtract(months=1)
        prev_week = now.subtract(weeks=1)

        DATE_MAPPER = {
            ReportPeriod.this_month: (
                now.start_of("month"),
                now,
            ),
            ReportPeriod.prev_month: (
                prev_month.start_of("month"),
                prev_month.end_of("month"),
            ),
            ReportPeriod.this_week: (
                now.start_of("week"),
                now,
            ),
            ReportPeriod.prev_week: (
                prev_week.start_of("week"),
                prev_week.end_of("week"),
            ),
        }

        start, end = DATE_MAPPER[period]
        events = await get_events(
            gcal, start, end, executor=executor
        )

        file_report, msg_report = await form_report(
            events, executor=executor
        )
        await msg.reply_document(
            file_report, msg_report
        )
        await rm(
            file_report.file.name, executor=executor
        )

    return report_handler
