"""change_selected_field_to_bigint

Revision ID: 2aef30611a72
Revises: 5ec048f750bf
Create Date: 2025-08-24 14:31:27.575614

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2aef30611a72"
down_revision: str | Sequence[str] | None = "5ec048f750bf"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # Change selected field from Integer to BigInteger to handle large values
    op.alter_column(
        "player_gameweek_history",
        "selected",
        existing_type=sa.Integer(),
        type_=sa.BigInteger(),
        existing_nullable=True,
    )


def downgrade() -> None:
    """Downgrade schema."""
    # Revert selected field back to Integer
    op.alter_column(
        "player_gameweek_history",
        "selected",
        existing_type=sa.BigInteger(),
        type_=sa.Integer(),
        existing_nullable=True,
    )
