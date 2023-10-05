"""add issues table

Revision ID: 51c2a045e971
Revises:
Create Date: 2023-10-05 23:43:48.590899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51c2a045e971'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'issues',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=True),
        sa.Column('created_at', sa.TIMESTAMP, nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=True),
    )


def downgrade():
    op.drop_table('issues')
