"""Recreate complete database schema

Revision ID: recreate_complete_schema
Revises: clean_base
Create Date: 2025-08-28 16:00:00.000000

"""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "recreate_complete_schema"
down_revision: str | Sequence[str] | None = "clean_base"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Create complete database schema."""

    # Create teams table
    op.create_table(
        "teams",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("short_name", sa.String(length=20), nullable=False),
        sa.Column("strength_attack_home", sa.Integer(), nullable=True),
        sa.Column("strength_attack_away", sa.Integer(), nullable=True),
        sa.Column("strength_defence_home", sa.Integer(), nullable=True),
        sa.Column("strength_defence_away", sa.Integer(), nullable=True),
        sa.Column("strength_overall_home", sa.Integer(), nullable=True),
        sa.Column("strength_overall_away", sa.Integer(), nullable=True),
        sa.Column("fpl_id", sa.Integer(), nullable=False),
        sa.Column("code", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("fpl_id", name="ix_teams_fpl_id"),
        sa.UniqueConstraint("name", name="uq_teams_name"),
    )

    # Create all_players table
    op.create_table(
        "all_players",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", name="uq_all_players_name"),
    )

    # Create players table
    op.create_table(
        "players",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("first_name", sa.String(length=100), nullable=False),
        sa.Column("second_name", sa.String(length=100), nullable=False),
        sa.Column("web_name", sa.String(length=100), nullable=True),
        sa.Column("team_id", sa.Integer(), nullable=False),
        sa.Column("element_type", sa.Integer(), nullable=False),
        sa.Column("now_cost", sa.Integer(), nullable=True),
        sa.Column("fpl_id", sa.Integer(), nullable=False),
        sa.Column("all_player_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("fpl_id", name="ix_players_fpl_id"),
        sa.ForeignKeyConstraint(
            ["all_player_id"],
            ["all_players.id"],
            name="fk_players_all_player_id_all_players",
        ),
    )

    # Create player_season_history table
    op.create_table(
        "player_season_history",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("player_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("season_name", sa.String(length=10), nullable=False),
        sa.Column("start_cost", sa.Integer(), nullable=True),
        sa.Column("end_cost", sa.Integer(), nullable=True),
        sa.Column("total_points", sa.Integer(), nullable=True),
        sa.Column("minutes", sa.Integer(), nullable=True),
        sa.Column("goals_scored", sa.Integer(), nullable=True),
        sa.Column("assists", sa.Integer(), nullable=True),
        sa.Column("clean_sheets", sa.Integer(), nullable=True),
        sa.Column("goals_conceded", sa.Integer(), nullable=True),
        sa.Column("own_goals", sa.Integer(), nullable=True),
        sa.Column("penalties_saved", sa.Integer(), nullable=True),
        sa.Column("penalties_missed", sa.Integer(), nullable=True),
        sa.Column("yellow_cards", sa.Integer(), nullable=True),
        sa.Column("red_cards", sa.Integer(), nullable=True),
        sa.Column("saves", sa.Integer(), nullable=True),
        sa.Column("bonus", sa.Integer(), nullable=True),
        sa.Column("bps", sa.Integer(), nullable=True),
        sa.Column("influence", sa.Float(), nullable=True),
        sa.Column("creativity", sa.Float(), nullable=True),
        sa.Column("threat", sa.Float(), nullable=True),
        sa.Column("ict_index", sa.Float(), nullable=True),
        sa.Column("all_player_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["all_player_id"],
            ["all_players.id"],
            name="fk_player_season_history_all_player_id_all_players",
        ),
    )

    # Create player_gameweek_history table
    op.create_table(
        "player_gameweek_history",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("player_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("gameweek", sa.Integer(), nullable=False),
        sa.Column("season", sa.String(length=10), nullable=False),
        sa.Column("fixture_id", sa.Integer(), nullable=False),
        sa.Column("opponent_team_id", sa.Integer(), nullable=False),
        sa.Column("total_points", sa.Integer(), nullable=False),
        sa.Column("was_home", sa.Boolean(), nullable=False),
        sa.Column("kickoff_time", sa.DateTime(), nullable=True),
        sa.Column("team_h_score", sa.Integer(), nullable=True),
        sa.Column("team_a_score", sa.Integer(), nullable=True),
        sa.Column("minutes", sa.Integer(), nullable=False),
        sa.Column("goals_scored", sa.Integer(), nullable=False),
        sa.Column("assists", sa.Integer(), nullable=False),
        sa.Column("clean_sheets", sa.Integer(), nullable=False),
        sa.Column("goals_conceded", sa.Integer(), nullable=False),
        sa.Column("own_goals", sa.Integer(), nullable=False),
        sa.Column("penalties_saved", sa.Integer(), nullable=False),
        sa.Column("penalties_missed", sa.Integer(), nullable=False),
        sa.Column("yellow_cards", sa.Integer(), nullable=False),
        sa.Column("red_cards", sa.Integer(), nullable=False),
        sa.Column("saves", sa.Integer(), nullable=False),
        sa.Column("bonus", sa.Integer(), nullable=False),
        sa.Column("bps", sa.Integer(), nullable=False),
        sa.Column("influence", sa.Float(), nullable=True),
        sa.Column("creativity", sa.Float(), nullable=True),
        sa.Column("threat", sa.Float(), nullable=True),
        sa.Column("ict_index", sa.Float(), nullable=True),
        sa.Column("value", sa.Integer(), nullable=True),
        sa.Column("selected", sa.BigInteger(), nullable=True),
        sa.Column("all_player_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "player_id", "gameweek", "season", name="uq_player_gameweek_season"
        ),
        sa.ForeignKeyConstraint(
            ["all_player_id"],
            ["all_players.id"],
            name="fk_player_gameweek_history_all_player_id_all_players",
        ),
    )

    # Create individual season tables
    seasons = [
        "2016_17",
        "2017_18",
        "2018_19",
        "2019_20",
        "2020_21",
        "2021_22",
        "2022_23",
        "2023_24",
        "2024_25",
    ]

    for season in seasons:
        op.create_table(
            f"player_gameweek_history_{season}",
            sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
            sa.Column("name", sa.String(), nullable=True),
            sa.Column("position", sa.String(), nullable=True),
            sa.Column("team", sa.String(), nullable=True),
            sa.Column("xP", sa.Float(), nullable=True),
            sa.Column("assists", sa.Integer(), nullable=True),
            sa.Column("bonus", sa.Integer(), nullable=True),
            sa.Column("bps", sa.Integer(), nullable=True),
            sa.Column("clean_sheets", sa.Integer(), nullable=True),
            sa.Column("creativity", sa.Float(), nullable=True),
            sa.Column("element", sa.Integer(), nullable=True),
            sa.Column("expected_assists", sa.Float(), nullable=True),
            sa.Column("expected_goal_involvements", sa.Float(), nullable=True),
            sa.Column("expected_goals", sa.Float(), nullable=True),
            sa.Column("expected_goals_conceded", sa.Float(), nullable=True),
            sa.Column("fixture", sa.Integer(), nullable=True),
            sa.Column("goals_conceded", sa.Integer(), nullable=True),
            sa.Column("goals_scored", sa.Integer(), nullable=True),
            sa.Column("ict_index", sa.Float(), nullable=True),
            sa.Column("influence", sa.Float(), nullable=True),
            sa.Column("kickoff_time", sa.String(), nullable=True),
            sa.Column("minutes", sa.Integer(), nullable=True),
            sa.Column("modified", sa.String(), nullable=True),
            sa.Column("opponent_team", sa.Integer(), nullable=True),
            sa.Column("own_goals", sa.Integer(), nullable=True),
            sa.Column("penalties_missed", sa.Integer(), nullable=True),
            sa.Column("penalties_saved", sa.Integer(), nullable=True),
            sa.Column("red_cards", sa.Integer(), nullable=True),
            sa.Column("round", sa.Integer(), nullable=True),
            sa.Column("saves", sa.Integer(), nullable=True),
            sa.Column("selected", sa.BigInteger(), nullable=True),
            sa.Column("starts", sa.Integer(), nullable=True),
            sa.Column("team_a_score", sa.Integer(), nullable=True),
            sa.Column("team_h_score", sa.Integer(), nullable=True),
            sa.Column("threat", sa.Float(), nullable=True),
            sa.Column("total_points", sa.Integer(), nullable=True),
            sa.Column("transfers_balance", sa.Integer(), nullable=True),
            sa.Column("transfers_in", sa.Integer(), nullable=True),
            sa.Column("transfers_out", sa.Integer(), nullable=True),
            sa.Column("value", sa.Integer(), nullable=True),
            sa.Column("was_home", sa.Boolean(), nullable=True),
            sa.Column("yellow_cards", sa.Integer(), nullable=True),
            sa.Column("GW", sa.Integer(), nullable=True),
            sa.Column("all_player_id", postgresql.UUID(as_uuid=True), nullable=True),
            sa.PrimaryKeyConstraint("id"),
            sa.ForeignKeyConstraint(
                ["all_player_id"],
                ["all_players.id"],
                name=f"fk_player_gameweek_history_{season}_all_player_id",
            ),
        )

    # Create data_events table
    op.create_table(
        "data_events",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("event_type", sa.String(length=50), nullable=False),
        sa.Column("table_name", sa.String(length=100), nullable=False),
        sa.Column("record_id", sa.String(length=100), nullable=False),
        sa.Column("old_values", sa.Text(), nullable=True),
        sa.Column("new_values", sa.Text(), nullable=True),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
        sa.Column("user_id", sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    # Create indexes
    op.create_index("ix_players_all_player_id", "players", ["all_player_id"])
    op.create_index("ix_players_web_name", "players", ["web_name"])
    op.create_index(
        "ix_player_season_history_all_player_id",
        "player_season_history",
        ["all_player_id"],
    )
    op.create_index(
        "ix_player_gameweek_history_all_player_id",
        "player_gameweek_history",
        ["all_player_id"],
    )
    op.create_index(
        "ix_player_gameweek_history_player_id", "player_gameweek_history", ["player_id"]
    )
    op.create_index(
        "ix_player_gameweek_history_gameweek", "player_gameweek_history", ["gameweek"]
    )
    op.create_index("ix_all_players_name", "all_players", ["name"])


def downgrade() -> None:
    """Remove all tables."""
    # Drop individual season tables first
    seasons = [
        "2016_17",
        "2017_18",
        "2018_19",
        "2019_20",
        "2020_21",
        "2021_22",
        "2022_23",
        "2023_24",
        "2024_25",
    ]

    for season in seasons:
        op.drop_table(f"player_gameweek_history_{season}")

    # Drop main tables
    op.drop_table("data_events")
    op.drop_table("player_gameweek_history")
    op.drop_table("player_season_history")
    op.drop_table("players")
    op.drop_table("all_players")
    op.drop_table("teams")
