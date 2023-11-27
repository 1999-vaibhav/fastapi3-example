"""add user table

Revision ID: e79c7ddba591
Revises: e8e4f818eed5
Create Date: 2023-11-24 16:02:17.093484

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e79c7ddba591'
down_revision: Union[str, None] = 'e8e4f818eed5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade(): op.create_table('users', sa.Column('id', sa.Integer, nullable=False),
                               sa.Column('email', sa.String(), nullable=False),
                               sa.Column('password', sa.String(),
                                         nullable=False),
                               sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                         server_default=sa.text('now()'), nullable=False),
                               sa.PrimaryKeyConstraint('id'),
                               sa.UniqueConstraint('email')
                               )


pass


def downgrade(): op.drop_table('users')


pass