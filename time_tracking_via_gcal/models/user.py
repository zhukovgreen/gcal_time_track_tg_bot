import sqlalchemy as sa
from sqlalchemy.schema import Table

from .base import Base


class User(Base):

    __tablename__ = "users"

    user_id = sa.Column(
        sa.Integer(), primary_key=True, unique=True
    )
    tags = sa.Column(sa.ARRAY(sa.String))
    currency = sa.Column(sa.String(3))
    rate = sa.Column(sa.Float())

    # username = sa.Column(
    #     sa.String(64), nullable=False, unique=True
    # )
    # email = sa.Column(
    #     sa.String(), nullable=False, unique=True
    # )
    # password = sa.Column(
    #     sa.String(255), nullable=False
    # )

    # api_token = sa.Column(sa.String(), nullable=False)

    # api_refresh_token = sa.Column(
    #     sa.String(), nullable=False
    # )


UserTable: Table = User.__table__
