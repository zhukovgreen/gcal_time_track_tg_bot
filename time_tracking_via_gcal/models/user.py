import sqlalchemy as sa
from sqlalchemy.schema import Table
from sqlalchemy.dialects.postgresql import BYTEA

from .base import Base


class User(Base):

    __tablename__ = "users"

    user_id = sa.Column(
        sa.Integer(), primary_key=True, unique=True
    )
    cal_id = sa.Column(sa.String())
    secrets = sa.Column(sa.JSON())
    cal_service = sa.Column(BYTEA())


UserTable: Table = User.__table__
