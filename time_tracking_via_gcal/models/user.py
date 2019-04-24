import sqlalchemy as sa
from sqlalchemy.schema import Table

from .base import Base


class User(Base):

    __tablename__ = "users"

    user_id = sa.Column(
        sa.Integer(), primary_key=True, unique=True
    )


UserTable: Table = User.__table__
