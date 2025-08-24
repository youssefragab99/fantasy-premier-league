"""add_code_field_to_teams

Revision ID: 4cb1f2f0358b
Revises: 2aef30611a72
Create Date: 2025-08-24 14:35:27.575614

"""

from collections.abc import Sequence
from contextlib import suppress

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4cb1f2f0358b"
down_revision: str | Sequence[str] | None = "2aef30611a72"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # Add code field to teams table
    op.add_column("teams", sa.Column("code", sa.Integer(), nullable=True))
    op.create_index(op.f("ix_teams_code"), "teams", ["code"], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    # Remove code field from teams table
    # Use raw SQL to avoid transaction issues
    connection = op.get_bind()

    # Drop the index if it exists (ignore errors)
    with suppress(Exception):
        connection.execute(sa.text("DROP INDEX IF EXISTS ix_teams_code"))

    # Drop the column if it exists (ignore errors)
    with suppress(Exception):
        connection.execute(
            sa.text("ALTER TABLE teams DROP COLUMN IF EXISTS code")
        )
