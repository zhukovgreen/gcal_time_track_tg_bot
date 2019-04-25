from concurrent.futures import ThreadPoolExecutor
import logging
from aiogram import types
from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

import pendulum

from ..utils.gcal_manager import get_events
from ..utils.rm import rm
from .utils.data_processing import form_report
from ..models.dal import (
    get_report_settings,
    get_user_cal_resources,
)
from .service import ReportPeriod


logger = logging.getLogger("aiogram")


def report_handler_factory(
    period: ReportPeriod, executor: ThreadPoolExecutor
):
    async def report_handler(msg: types.Message):
        gcal, cal_id = await get_user_cal_resources(
            msg.from_user.id
        )
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
            gcal,
            cal_id,
            start,
            end,
            executor=executor,
        )

        report_settings = await get_report_settings(
            msg
        )
        tags: tuple = report_settings["tags"]
        currency: str = report_settings["currency"]
        rate: float = report_settings["rate"]
        file_report, msg_report = await form_report(
            events,
            tags,
            rate,
            currency,
            executor=executor,
        )
        await msg.reply_document(
            file_report, msg_report
        )
        await rm(
            file_report.file.name, executor=executor
        )

    return report_handler
