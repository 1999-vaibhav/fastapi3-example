"""create posts table

Revision ID: c623d5e71d67
Revises: 
Create Date: 2023-11-24 15:39:52.497360

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c623d5e71d67'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(): op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                                                  primary_key=True), sa.Column('title', sa.String(), nullable=False))


pass


def downgrade():
    op.drop_table('posts')
    pass
