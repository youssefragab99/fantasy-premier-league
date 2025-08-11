"""applying_event_trigger_to_tables

Revision ID: 529a87fbd22a
Revises: 76bc4cebde78
Create Date: 2025-08-11 13:40:00.665379

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "529a87fbd22a"
down_revision: Union[str, Sequence[str], None] = "76bc4cebde78"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# --- MANAGE YOUR AUDITED TABLES HERE ---
# Simply add or remove table names from this list.
TABLES_TO_AUDIT = [
    "players",
    "teams",
    "player_gameweek_history",
]
# ----------------------------------------


def upgrade() -> None:
    """Upgrade schema."""
    for table_name in TABLES_TO_AUDIT:
        op.execute(f"""
            CREATE TRIGGER {table_name}_audit_trigger
            AFTER INSERT OR UPDATE OR DELETE ON {table_name}
            FOR EACH ROW EXECUTE FUNCTION log_data_changes();
        """)


def downgrade() -> None:
    """Downgrade schema."""
    for table_name in TABLES_TO_AUDIT:
        op.execute(f"""
            DROP TRIGGER IF EXISTS {table_name}_audit_trigger ON {table_name};
        """)
