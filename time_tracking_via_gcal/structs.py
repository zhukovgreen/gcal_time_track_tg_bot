from enum import Enum


class States(Enum):
    AUTH_CAL_ID: str = "AUTH_CAL_ID"
    AUTH_SECRETS: str = "AUTH_SECRETS"
    EDIT: str = "EDIT"
    VIEWING: str = "VIEWING"


class ReportPeriod(Enum):
    prev_month: str = "previous month"
    this_month: str = "this month"
    prev_week: str = "previous week"
    this_week: str = "this week"
