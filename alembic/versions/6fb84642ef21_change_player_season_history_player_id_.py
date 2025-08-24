"""change_player_season_history_player_id_to_uuid

Revision ID: 6fb84642ef21
Revises: 81d12b798359
Create Date: 2025-08-24 18:35:49.904656

"""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6fb84642ef21"
down_revision: str | Sequence[str] | None = "81d12b798359"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # Add a new UUID column for player_id
    op.add_column(
        "player_season_history",
        sa.Column("player_id_uuid", postgresql.UUID(as_uuid=True), nullable=True),
    )

    # Populate the new UUID column by joining with the players table
    op.execute(
        """
        UPDATE player_season_history 
        SET player_id_uuid = players.id 
        FROM players 
        WHERE player_season_history.player_id = players.fpl_id
    """
    )

    # Make the new column not nullable
    op.alter_column("player_season_history", "player_id_uuid", nullable=False)

    # Drop the old integer column
    op.drop_column("player_season_history", "player_id")

    # Rename the new column to the original name
    op.alter_column("player_season_history", "player_id_uuid", new_column_name="player_id")


def downgrade() -> None:
    """Downgrade schema."""
    # Add back the integer column
    op.add_column("player_season_history", sa.Column("player_id_int", sa.Integer(), nullable=True))

    # Populate it by joining with players table using fpl_id
    op.execute(
        """
        UPDATE player_season_history 
        SET player_id_int = players.fpl_id 
        FROM players 
        WHERE player_season_history.player_id = players.id
    """
    )

    # Make it not nullable
    op.alter_column("player_season_history", "player_id_int", nullable=False)

    # Drop the UUID column
    op.drop_column("player_season_history", "player_id")

    # Rename the integer column back to the original name
    op.alter_column("player_season_history", "player_id_int", new_column_name="player_id")
