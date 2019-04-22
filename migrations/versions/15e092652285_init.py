"""init

Revision ID: 15e092652285
Revises: 1924a11946f8
Create Date: 2019-04-15 17:07:58.290435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15e092652285'
down_revision = '1924a11946f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('tags', sa.ARRAY(sa.String()), nullable=True))
    op.add_column('users', sa.Column('user_id', sa.Integer(), nullable=False))
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.drop_column('users', 'api_refresh_token')
    op.drop_column('users', 'api_token')
    op.drop_column('users', 'password')
    op.drop_column('users', 'email')
    op.drop_column('users', 'username')
    op.drop_column('users', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('users', sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('api_token', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('api_refresh_token', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.drop_column('users', 'user_id')
    op.drop_column('users', 'tags')
    # ### end Alembic commands ###