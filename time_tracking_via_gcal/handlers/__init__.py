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

from ..gcal_manager import get_events
from .data_processing import form_report
from ..utils import rm


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


async def start(msg: types.Message):
    await msg.reply(
        "Main menu activated", reply_markup=main_menu
    )


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
