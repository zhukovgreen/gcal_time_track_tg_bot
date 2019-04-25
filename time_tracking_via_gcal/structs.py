from enum import Enum


class States(Enum):
    AUTH_CAL_ID: str = "AUTH_CAL_ID"
    AUTH_SECRETS: str = "AUTH_SECRETS"
    EDIT: str = "EDIT"
    VIEWING: str = "VIEWING"
