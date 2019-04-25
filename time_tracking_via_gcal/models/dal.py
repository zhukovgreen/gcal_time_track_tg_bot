import pickle
from aiogram.types import Message
from aiopg.sa.connection import SAConnection
from aiopg.sa.engine import Engine
from googleapiclient.discovery import Resource

from ..app import dp
from ..models import UserTable, ReportSettingsTable

# Types
GCalResource = Resource
GCalId = str

# Msgs


async def create_new_user(user_id: int):
    engine: Engine = dp["pg"]
    async with engine.acquire() as conn:
        conn: SAConnection
        await conn.execute(
            UserTable.insert().values(user_id=user_id)
        )
        await conn.execute(
            ReportSettingsTable.insert().values(
                user_id=user_id,
                tags=("", ""),
                currency="",
                rate=0,
            )
        )


async def get_report_settings(msg: Message) -> dict:
    engine: Engine = dp["pg"]
    async with engine.acquire() as conn:
        conn: SAConnection
        resp = await conn.execute(
            ReportSettingsTable.select().where(
                ReportSettingsTable.c.user_id
                == msg.from_user.id
            )
        )
        user_settings_resp = await resp.fetchone()

    settings: dict = dict(
        zip(
            ReportSettingsTable.columns.keys(),
            user_settings_resp.as_tuple(),
        )
    )
    del settings["user_id"]
    return settings


async def get_user_cal_resources(
    user_id: int
) -> (GCalResource, GCalId):
    engine: Engine = dp["pg"]
    async with engine.acquire() as conn:
        conn: SAConnection
        resp = await (
            await conn.execute(
                UserTable.select().where(
                    UserTable.c.user_id == user_id
                )
            )
        ).fetchone()

    resp = dict(
        zip(UserTable.columns.keys(), resp.as_tuple())
    )
    cal_service = pickle.loads(resp["cal_service"])
    return cal_service, resp["cal_id"]


async def get_user_cal_secrets(user_id: int) -> dict:
    engine: Engine = dp["pg"]
    async with engine.acquire() as conn:
        conn: SAConnection
        resp = await (
            await conn.execute(
                UserTable.select().where(
                    UserTable.c.user_id == user_id
                )
            )
        ).fetchone()

    resp = dict(
        zip(UserTable.columns.keys(), resp.as_tuple())
    )
    return resp["secrets"]


async def update_user(
    user_id: int,
    *,
    cal_id: str = None,
    secrets: dict = None,
    cal_service: bytes = None,
):
    engine: Engine = dp["pg"]
    async with engine.acquire() as conn:
        conn: SAConnection
        await conn.execute(
            UserTable.update()
            .where(UserTable.c.user_id == user_id)
            .values(
                **{
                    k: v
                    for k, v in zip(
                        [
                            "cal_id",
                            "secrets",
                            "cal_service",
                        ],
                        [
                            cal_id,
                            secrets,
                            cal_service,
                        ],
                    )
                    if v is not None
                }
            )
        )


async def update_report_settings(
    msg: Message,
    rate: float,
    currency: str,
    tags: tuple,
):
    engine: Engine = dp["pg"]
    async with engine.acquire() as conn:
        conn: SAConnection
        await conn.execute(
            ReportSettingsTable.update()
            .where(
                ReportSettingsTable.c.user_id
                == msg.from_user.id
            )
            .values(
                rate=rate,
                currency=currency,
                tags=tags,
            )
        )
