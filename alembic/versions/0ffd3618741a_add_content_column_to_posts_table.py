"""add content column to posts table

Revision ID: 0ffd3618741a
Revises: e03fb48b116a
Create Date: 2022-04-05 00:02:20.075379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ffd3618741a'
down_revision = 'e03fb48b116a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
