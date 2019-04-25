from functools import partial
from concurrent.futures import ThreadPoolExecutor
import asyncio
import logging
from typing import List
import datetime

from googleapiclient.discovery import build
from google.oauth2 import service_account


logger = logging.getLogger("aiogram")


SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly"
]


def build_gcal(secrets: dict):
    creds = service_account.Credentials.from_service_account_info(
        secrets
    )
    gcal = build(
        "calendar",
        "v3",
        credentials=creds,
        cache_discovery=False,
    )
    logger.debug(f"Google calendar was built")
    return gcal


def _get_events_worker(
    gcal,
    calendar_id: str,
    start: datetime.datetime,
    end: datetime.datetime,
) -> List[dict]:

    events_data = (
        gcal.events()
        .list(
            calendarId=calendar_id,
            timeMin=start.isoformat(),
            timeMax=end.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    return events_data.get("items", [])


async def get_events(
    gcal,
    calendar_id: str,
    start: datetime.datetime,
    end: datetime.datetime,
    executor: ThreadPoolExecutor,
) -> List[dict]:
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        executor,
        partial(
            _get_events_worker,
            gcal,
            calendar_id,
            start,
            end,
        ),
    )
