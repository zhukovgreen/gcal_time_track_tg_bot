import sqlalchemy as sa
from sqlalchemy.schema import Table, ForeignKey

from .base import Base
from .user import UserTable


class UserSettings(Base):

    __tablename__ = "user_settings"

    user_id = sa.Column(
        ForeignKey(UserTable.c.user_id),
        primary_key=True,
        unique=True,
    )
    tags = sa.Column(sa.ARRAY(sa.String))
    currency = sa.Column(sa.String(3))
    rate = sa.Column(sa.Float())


UserSettingsTable: Table = UserSettings.__table__
