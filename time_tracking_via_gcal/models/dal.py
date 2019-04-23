from aiogram.types import Message
from psycopg2 import errors
from aiopg.sa.connection import SAConnection
from aiopg.sa.engine import Engine

from .app import dp


async def create_new_user(msg: Message):
    engine: Engine = dp["pg"]
    async with engine.acquire() as conn:
        conn: SAConnection

        try:
            await conn.execute(
                UserTable.insert().values(
                    user_id=msg.from_user.id
                )
            )
            await conn.execute(
                UserSettingsTable.insert().values(
                    user_id=msg.from_user.id,
                    tags=("", ""),
                    currency="",
                    rate=0,
                )
            )

        except errors.UniqueViolation:
            await msg.reply(
                "User with this id is already registered"
            )


async def get_user_settings(user_id: int) -> dict:

    engine: Engine = dp["pg"]
    async with engine.acquire() as conn:
        conn: SAConnection
        resp = await conn.execute(
            UserSettingsTable.select().where(
                UserSettingsTable.c.user_id
                == msg.from_user.id
            )
        )
        user_settings_resp = await resp.fetchone()

    settings: dict = dict(
        zip(
            UserSettingsTable.columns.keys(),
            user_settings_resp.as_tuple(),
        )
    )
    del settings["user_id"]
    return settings


async def update_user_settings(rate, currency, tags):
    engine: Engine = dp["pg"]
    async with engine.acquire() as conn:
        conn: SAConnection
        await conn.execute(
            UserSettingsTable.update()
            .where(
                UserSettingsTable.c.user_id
                == msg.from_user.id
            )
            .values(
                rate=rate,
                currency=currency,
                tags=tags,
            )
        )
