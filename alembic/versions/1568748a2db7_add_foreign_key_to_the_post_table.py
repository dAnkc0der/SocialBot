"""add foreign-key to the post table

Revision ID: 1568748a2db7
Revises: 7d4479d26bdd
Create Date: 2022-04-05 00:25:35.936309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1568748a2db7'
down_revision = '7d4479d26bdd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
