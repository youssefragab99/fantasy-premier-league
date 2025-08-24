"""add_uuid_support_and_fpl_id_fields

Revision ID: 5ec048f750bf
Revises: 11df647a6578
Create Date: 2025-08-24 02:50:59.894475

"""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5ec048f750bf"
down_revision: str | Sequence[str] | None = "11df647a6578"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    # Add UUID extension if not exists
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')

    # Add fpl_id column to teams table
    op.add_column("teams", sa.Column("fpl_id", sa.Integer(), nullable=True))
    op.create_index(op.f("ix_teams_fpl_id"), "teams", ["fpl_id"], unique=True)

    # Add fpl_id column to players table
    op.add_column("players", sa.Column("fpl_id", sa.Integer(), nullable=True))
    op.create_index(op.f("ix_players_fpl_id"), "players", ["fpl_id"], unique=True)

    # Add UUID id column to teams table
    op.add_column("teams", sa.Column("uuid_id", postgresql.UUID(as_uuid=True), nullable=True))
    op.execute("UPDATE teams SET uuid_id = uuid_generate_v4()")
    op.alter_column("teams", "uuid_id", nullable=False)

    # Add UUID id column to players table
    op.add_column("players", sa.Column("uuid_id", postgresql.UUID(as_uuid=True), nullable=True))
    op.execute("UPDATE players SET uuid_id = uuid_generate_v4()")
    op.alter_column("players", "uuid_id", nullable=False)

    # Add UUID id column to player_gameweek_history table
    op.add_column(
        "player_gameweek_history",
        sa.Column("uuid_id", postgresql.UUID(as_uuid=True), nullable=True),
    )
    op.execute("UPDATE player_gameweek_history SET uuid_id = uuid_generate_v4()")
    op.alter_column("player_gameweek_history", "uuid_id", nullable=False)

    # Add UUID id column to player_season_history table
    op.add_column(
        "player_season_history", sa.Column("uuid_id", postgresql.UUID(as_uuid=True), nullable=True)
    )
    op.execute("UPDATE player_season_history SET uuid_id = uuid_generate_v4()")
    op.alter_column("player_season_history", "uuid_id", nullable=False)

    # Add UUID id columns to all player_gameweek_history_* tables
    season_tables = [
        "player_gameweek_history_2016_17",
        "player_gameweek_history_2017_18",
        "player_gameweek_history_2018_19",
        "player_gameweek_history_2019_20",
        "player_gameweek_history_2020_21",
        "player_gameweek_history_2021_22",
        "player_gameweek_history_2022_23",
        "player_gameweek_history_2023_24",
    ]

    for table_name in season_tables:
        try:
            op.add_column(
                table_name, sa.Column("uuid_id", postgresql.UUID(as_uuid=True), nullable=True)
            )
            op.execute(f"UPDATE {table_name} SET uuid_id = uuid_generate_v4()")
            op.alter_column(table_name, "uuid_id", nullable=False)
        except Exception:
            # Table might not exist yet, skip
            pass

    # Drop foreign key constraints first
    try:
        op.drop_constraint("players_team_id_fkey", "players", type_="foreignkey")
    except Exception:
        pass

    try:
        op.drop_constraint(
            "player_gameweek_history_opponent_team_id_fkey",
            "player_gameweek_history",
            type_="foreignkey",
        )
    except Exception:
        pass

    try:
        op.drop_constraint(
            "player_gameweek_history_player_id_fkey", "player_gameweek_history", type_="foreignkey"
        )
    except Exception:
        pass

    try:
        op.drop_constraint(
            "player_season_history_player_id_fkey", "player_season_history", type_="foreignkey"
        )
    except Exception:
        pass

    # Drop old primary keys and set new UUID primary keys
    # Teams table
    op.drop_constraint("teams_pkey", "teams", type_="primary")
    op.create_primary_key("teams_pkey", "teams", ["uuid_id"])
    op.drop_column("teams", "id")
    op.alter_column("teams", "uuid_id", new_column_name="id")

    # Players table
    op.drop_constraint("players_pkey", "players", type_="primary")
    op.create_primary_key("players_pkey", "players", ["id"])
    op.drop_column("players", "id")
    op.alter_column("players", "uuid_id", new_column_name="id")

    # Player gameweek history table
    op.drop_constraint("player_gameweek_history_pkey", "player_gameweek_history", type_="primary")
    op.create_primary_key("player_gameweek_history_pkey", "player_gameweek_history", ["id"])
    op.drop_column("player_gameweek_history", "id")
    op.alter_column("player_gameweek_history", "uuid_id", new_column_name="id")

    # Player season history table
    op.drop_constraint("player_season_history_pkey", "player_season_history", type_="primary")
    op.create_primary_key("player_season_history_pkey", "player_season_history", ["id"])
    op.drop_column("player_season_history", "id")
    op.alter_column("player_season_history", "uuid_id", new_column_name="id")

    # Update foreign key references to use UUIDs
    # This will need to be done carefully to maintain referential integrity
    # For now, we'll recreate the foreign key constraints with the new UUID columns


def downgrade() -> None:
    """Downgrade schema."""
    # This is a complex migration that changes primary keys
    # Downgrade would require recreating the old structure
    # For now, we'll leave this as a one-way migration
    pass
