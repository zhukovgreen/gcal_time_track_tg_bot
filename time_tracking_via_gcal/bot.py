import os
import logging
from concurrent.futures import ThreadPoolExecutor
import asyncio

import attr
from aiogram import executor, types
from googleapiclient.discovery import Resource

from .handlers import (
    echo,
    report_handler_factory,
    start,
    ReportPeriod,
)
from .app import bot, dp
from .handlers.settings import settings, settings_edit
from .settings import PATH
from .gcal_manager import build_gcal


logger = logging.getLogger("aiogram")


def _period_check_factory(period: ReportPeriod):
    def period_check(msg: types.Message) -> bool:
        return (
            True
            if msg.text == period.value
            else False
        )

    return period_check


@attr.s(auto_attribs=True)
class BotManager:
    gcal: Resource = attr.ib(init=False)
    executor_pool: ThreadPoolExecutor = attr.ib(
        init=False
    )

    def start(self):
        executor.start_polling(
            dp,
            on_startup=self.on_startup,
            on_shutdown=self.on_shutdown,
        )

    async def on_startup(self, _):
        self.gcal = build_gcal()
        self.executor_pool = ThreadPoolExecutor()
        await self._register_handlers()

    async def on_shutdown(self, _):
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.close()
        self.executor_pool.shutdown()
        for f in os.listdir(PATH / "tmp"):
            os.remove(PATH / "tmp" / f)
        await asyncio.sleep(0.250)

    async def _register_handlers(self):
        dp.register_message_handler(
            start, commands=["start"]
        )
        dp.register_message_handler(
            echo, commands=["_echo"]
        )
        for period in ReportPeriod:
            period: ReportPeriod
            dp.register_message_handler(
                report_handler_factory(
                    period,
                    self.executor_pool,
                    self.gcal,
                ),
                _period_check_factory(period),
            )
        logger.info("registering handlers succseeded")
        dp.register_message_handler(
            settings, commands="settings"
        )
        dp.register_callback_query_handler(
            settings_edit,
            lambda c: c.data == "edit_settings",
        )


def run_bot():
    bot = BotManager()
    bot.start()
