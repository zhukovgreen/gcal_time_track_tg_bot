import uuid
import asyncio
from concurrent.futures import ThreadPoolExecutor
import datetime
import random

import numpy as np
import pandas as pd
from aiogram import types


def _form_report_worker(
    events, tags, rate, currency
) -> (types.InputFile, str):
    events_df = pd.DataFrame(events)
    report: pd.DataFrame = process_data(
        events_df, tags=tags, rate=rate
    )
    report_pt_long = pd.pivot_table(
        report,
        values=["meeting_length", "amount_due"],
        index=[
            f"G{idx+1}" for idx, _ in enumerate(tags)
        ]
        + ["start", "summary"],
        margins=True,
        aggfunc=np.sum,
    )
    report_pt_long["amount_due"] = (
        report_pt_long["amount_due"]
        .round(2)
        .astype(str)
        + " "
        + currency
    )
    csv_file = f"./tmp/{str(uuid.uuid4())}.csv"
    report_pt_long.to_csv(csv_file)

    report_pt_short = pd.pivot_table(
        report,
        values=["meeting_length", "amount_due"],
        index=[
            f"G{idx+1}" for idx, _ in enumerate(tags)
        ],
        margins=True,
        aggfunc=np.sum,
    )

    return (
        types.InputFile(csv_file, filename="out.csv"),
        report_pt_short.to_string(
            formatters=[
                lambda x: r"{:.2f} {}".format(
                    float(x), currency
                ),
                lambda x: r"{:.1f} h".format(
                    float(x)
                ),
            ]
        ),
    )


def process_data(
    data: pd.DataFrame,
    tags: tuple = ("", ""),
    rate: float = 0,
    currency: str = "",
    *,
    modify_summary: bool = False,
) -> pd.DataFrame:
    data["start"] = data["start"].apply(
        from_json_date_str
    )
    data["end"] = data["end"].apply(
        from_json_date_str
    )
    data["summary"] = data["summary"].str.lower()
    data["meeting_length"] = (
        data["end"] - data["start"]
    ) / np.timedelta64(1, "h")

    if modify_summary:
        data["summary"] = data["summary"].apply(
            summary_modifier
        )

    reg = (
        "^(?P<summary>.*?) "
        + " ".join(
            [
                f"(?P<G{idx+1}>\[{tag}.*?\])"
                for idx, tag in enumerate(tags)
            ]
        )
        + "$"
    )
    data[
        ["summary"]
        + [f"G{idx+1}" for idx, _ in enumerate(tags)]
    ] = data["summary"].str.extract(reg, expand=True)
    data["amount_due"] = data["meeting_length"] * rate
    return data


def from_json_date_str(data):
    return datetime.datetime.fromisoformat(
        data["dateTime"]
    )


def summary_modifier(data):
    tk = data.split()
    tk += [
        random.choice([r"[gc]", r"[tbe]"]),
        random.choice(
            [
                r"[rnd]",
                r"[dev]",
                r"[test]",
                r"[doc]",
                r"[bugfix]",
            ]
        ),
    ]

    return " ".join(tk)


async def form_report(
    events,
    tags: tuple = ("", ""),
    rate: float = 0,
    currency: str = "",
    executor: ThreadPoolExecutor = None,
) -> (types.InputFile, str):
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        executor,
        _form_report_worker,
        events,
        tags,
        rate,
        currency,
    )
