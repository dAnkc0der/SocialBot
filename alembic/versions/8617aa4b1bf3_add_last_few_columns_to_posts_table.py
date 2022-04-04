"""add last few columns to posts table

Revision ID: 8617aa4b1bf3
Revises: 1568748a2db7
Create Date: 2022-04-05 00:35:04.691338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8617aa4b1bf3'
down_revision = '1568748a2db7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
