"""create table

Revision ID: 9e53568cac2c
Revises:
Create Date: 2021-04-10 15:03:25.343055

"""
from alembic import op
import sqlalchemy as sa


revision = "9e53568cac2c"
down_revision = None
branch_labels = None
depends_on = None


def create_users_table() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.Text, unique=True, nullable=False, index=True),
        sa.Column("password", sa.Text),
    )


def upgrade() -> None:
    create_users_table()


def downgrade() -> None:
    op.drop_table("users")
