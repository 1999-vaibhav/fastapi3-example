"""add content column to   posts table

Revision ID: e8e4f818eed5
Revises: c623d5e71d67
Create Date: 2023-11-24 15:55:39.358396

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8e4f818eed5'
down_revision: Union[str, None] = 'c623d5e71d67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
pass


def downgrade():op.drop_column('posts','content')
pass
