"""made name field in Author model uniq

Revision ID: 8a9aee33ee92
Revises: fa73e4faf7f5
Create Date: 2025-11-25 21:32:21.326743

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a9aee33ee92'
down_revision: Union[str, Sequence[str], None] = 'fa73e4faf7f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table("authors", schema=None) as batch_op:
        batch_op.create_unique_constraint("uq_authors_name", ["name"])


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table("authors", schema=None) as batch_op:
        batch_op.drop_constraint("uq_authors_name", type_="unique")
