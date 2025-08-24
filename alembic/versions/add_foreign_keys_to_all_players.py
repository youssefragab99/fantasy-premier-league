"""Add foreign keys to all_players table

Revision ID: add_foreign_keys_to_all_players
Revises: 11df647a6578
Create Date: 2024-12-19 10:00:00.000000

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "add_foreign_keys_to_all_players"
down_revision = "fix_all_players_table_structure"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Add foreign key constraints to all_players table."""

    # Add all_player_id column to players table if it doesn't exist
    op.add_column("players", sa.Column("all_player_id", postgresql.UUID(as_uuid=True), nullable=True))
    op.create_index(op.f("ix_players_all_player_id"), "players", ["all_player_id"], unique=False)

    # Add all_player_id column to player_gameweek_history table if it doesn't exist
    op.add_column(
        "player_gameweek_history",
        sa.Column("all_player_id", postgresql.UUID(as_uuid=True), nullable=True),
    )
    op.create_index(
        op.f("ix_player_gameweek_history_all_player_id"),
        "player_gameweek_history",
        ["all_player_id"],
        unique=False,
    )

    # Add all_player_id column to player_season_history table if it doesn't exist
    op.add_column(
        "player_season_history",
        sa.Column("all_player_id", postgresql.UUID(as_uuid=True), nullable=True),
    )
    op.create_index(
        op.f("ix_player_season_history_all_player_id"),
        "player_season_history",
        ["all_player_id"],
        unique=False,
    )

    # Add foreign key constraints
    op.create_foreign_key(
        "fk_players_all_player_id_all_players", "players", "all_players", ["all_player_id"], ["id"]
    )

    op.create_foreign_key(
        "fk_player_gameweek_history_all_player_id_all_players",
        "player_gameweek_history",
        "all_players",
        ["all_player_id"],
        ["id"],
    )

    op.create_foreign_key(
        "fk_player_season_history_all_player_id_all_players",
        "player_season_history",
        "all_players",
        ["all_player_id"],
        ["id"],
    )


def downgrade() -> None:
    """Remove foreign key constraints from all_players table."""

    # Remove foreign key constraints
    op.drop_constraint(
        "fk_player_season_history_all_player_id_all_players",
        "player_season_history",
        type_="foreignkey",
    )
    op.drop_constraint(
        "fk_player_gameweek_history_all_player_id_all_players",
        "player_gameweek_history",
        type_="foreignkey",
    )
    op.drop_constraint("fk_players_all_player_id_all_players", "players", type_="foreignkey")

    # Remove indexes
    op.drop_index(
        op.f("ix_player_season_history_all_player_id"), table_name="player_season_history"
    )
    op.drop_index(
        op.f("ix_player_gameweek_history_all_player_id"), table_name="player_gameweek_history"
    )
    op.drop_index(op.f("ix_players_all_player_id"), table_name="players")

    # Remove columns
    op.drop_column("player_season_history", "all_player_id")
    op.drop_column("player_gameweek_history", "all_player_id")
    op.drop_column("players", "all_player_id")
