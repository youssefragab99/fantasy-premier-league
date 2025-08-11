"""Add player_season_history table

Revision ID: 2692fb6146b7
Revises: 529a87fbd22a
Create Date: 2025-08-11 15:22:52.969093

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "2692fb6146b7"
down_revision: Union[str, Sequence[str], None] = "529a87fbd22a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "player_season_history",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("player_id", sa.Integer(), nullable=False),
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
        sa.ForeignKeyConstraint(
            ["player_id"],
            ["players.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("player_id", "season_name", name="uq_player_season"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("player_season_history")
