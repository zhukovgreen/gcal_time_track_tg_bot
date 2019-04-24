from functools import partial
from concurrent.futures import ThreadPoolExecutor
import asyncio
import logging
from typing import List
import datetime
import pickle

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from ..settings import PATH


logger = logging.getLogger("aiogram")


SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly"
]


def build_gcal():
    if (PATH / "token.pickle").exists:
        with open(
            PATH / "token.pickle", "rb"
        ) as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available,
    # let the user log in.
    if not creds or not creds.valid:
        if (
            creds
            and creds.expired
            and creds.refresh_token
        ):
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                PATH / "credentials.json", SCOPES
            )
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open(
            PATH / "token.pickle", "wb"
        ) as token:
            pickle.dump(creds, token)
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
    start: datetime.datetime,
    end: datetime.datetime,
) -> List[dict]:

    events_data = (
        gcal.events()
        .list(
            calendarId="primary",
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
    start: datetime.datetime,
    end: datetime.datetime,
    executor: ThreadPoolExecutor,
) -> List[dict]:
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        executor,
        partial(_get_events_worker, gcal, start, end),
    )
