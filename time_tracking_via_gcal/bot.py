import os
import logging
from concurrent.futures import ThreadPoolExecutor
import asyncio

import attr
from aiogram import executor, types
from googleapiclient.discovery import Resource
from aiopg.sa import create_engine
from aiopg.sa.engine import Engine

from .handlers import (
    echo,
    report_handler_factory,
    reset_state,
    settings_edit_callback,
    settings_get,
    settings_set,
    start,
    ReportPeriod,
)
from .app import bot, dp
from .structs import States
from .settings import PATH, DB_DSN
from .utils.gcal_manager import build_gcal


logger = logging.getLogger("aiogram")


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
        dp["pg"]: Engine = await create_engine(
            dsn=str(DB_DSN)
        )
        await self._register_handlers()

    async def on_shutdown(self, _):
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.close()
        self.executor_pool.shutdown()
        for f in os.listdir(PATH / "tmp"):
            os.remove(PATH / "tmp" / f)
        await dp.storage.close()
        await dp.storage.wait_closed()
        pg: Engine = dp["pg"]
        pg.close()
        await asyncio.sleep(0.250)

    async def _register_handlers(self):
        dp.register_message_handler(
            start, commands=["start"]
        )
        dp.register_message_handler(
            echo, commands=["_echo"], state="*"
        )
        dp.register_message_handler(
            reset_state,
            commands=["_reset_state"],
            state="*",
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
                state=States.VIEWING.value,
            )
        dp.register_message_handler(
            settings_get,
            commands="settings",
            state=States.VIEWING.value,
        )
        dp.register_callback_query_handler(
            settings_edit_callback,
            lambda c: c.data == "edit_settings",
            state=States.VIEWING.value,
        )
        dp.register_message_handler(
            settings_set, state=States.EDIT.value
        )
        logger.info("registering handlers succseeded")


def _period_check_factory(period: ReportPeriod):
    def period_check(msg: types.Message) -> bool:
        return (
            True
            if msg.text == period.value
            else False
        )

    return period_check


def run_bot():
    bot = BotManager()
    bot.start()
