"""init

Revision ID: 80726396cd81
Revises: 40f7dcdf931b
Create Date: 2019-04-25 06:51:55.599350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "80726396cd81"
down_revision = "40f7dcdf931b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "cal_service", sa.JSON(), nullable=True
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "cal_service")
    # ### end Alembic commands ###