"""Clean base migration - represents current database state

Revision ID: clean_base
Revises:
Create Date: 2025-08-28 15:00:00.000000

"""

from collections.abc import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "clean_base"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema - this represents the current state."""
    # This migration represents the current database state
    # No changes needed since the schema is already correct
    pass


def downgrade() -> None:
    """Downgrade schema - remove all tables."""
    # Drop all tables in the correct order to avoid foreign key issues

    # Drop individual season tables first (they reference all_players)
    # Use raw SQL with IF EXISTS to handle cases where tables don't exist
    op.execute("DROP TABLE IF EXISTS player_gameweek_history_2024_25 CASCADE")
    op.execute("DROP TABLE IF EXISTS player_gameweek_history_2023_24 CASCADE")
    op.execute("DROP TABLE IF EXISTS player_gameweek_history_2022_23 CASCADE")
    op.execute("DROP TABLE IF EXISTS player_gameweek_history_2020_21 CASCADE")
    op.execute("DROP TABLE IF EXISTS player_gameweek_history_2019_20 CASCADE")
    op.execute("DROP TABLE IF EXISTS player_gameweek_history_2018_19 CASCADE")
    op.execute("DROP TABLE IF EXISTS player_gameweek_history_2017_18 CASCADE")
    op.execute("DROP TABLE IF EXISTS player_gameweek_history_2016_17 CASCADE")

    # Drop main tables
    op.execute("DROP TABLE IF EXISTS player_gameweek_history CASCADE")
    op.execute("DROP TABLE IF EXISTS player_season_history CASCADE")
    op.execute("DROP TABLE IF EXISTS players CASCADE")
    op.execute("DROP TABLE IF EXISTS all_players CASCADE")
    op.execute("DROP TABLE IF EXISTS teams CASCADE")
    op.execute("DROP TABLE IF EXISTS data_events CASCADE")
