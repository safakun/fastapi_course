"""New Migration

Revision ID: d5eed8bc089a
Revises: 65ca8c5c03b8
Create Date: 2024-03-04 11:08:14.395113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5eed8bc089a'
down_revision: Union[str, None] = '65ca8c5c03b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blogs', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'user_id')
    # ### end Alembic commands ###
