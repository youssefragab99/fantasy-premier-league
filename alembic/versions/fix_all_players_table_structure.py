"""Fix all_players table structure

Revision ID: fix_all_players_table_structure
Revises: 35e3aec009b9
Create Date: 2024-12-19 11:00:00.000000

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "fix_all_players_table_structure"
down_revision = "35e3aec009b9"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Fix the all_players table structure."""
    
    # First, drop the existing table and recreate it with proper structure
    # This is safe since all_players is just a reference table
    
    # Drop the existing table
    op.drop_table("all_players")
    
    # Create the table with proper structure
    op.create_table(
        "all_players",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name")
    )
    
    # Create index on name for performance
    op.create_index(op.f("ix_all_players_name"), "all_players", ["name"], unique=True)


def downgrade() -> None:
    """Revert the all_players table structure."""
    
    # Drop the properly structured table
    op.drop_index(op.f("ix_all_players_name"), table_name="all_players")
    op.drop_table("all_players")
    
    # Recreate the old structure (though this will lose data)
    op.create_table(
        "all_players",
        sa.Column("id", sa.String(), nullable=True),
        sa.Column("name", sa.String(), nullable=True)
    ) 