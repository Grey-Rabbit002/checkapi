"""teacher table created

Revision ID: 5c5b81202800
Revises: 
Create Date: 2023-04-23 17:39:38.276664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c5b81202800'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'teacher',
        sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
        sa.Column('dept_id',sa.Integer(),nullable=False),
        sa.Column('teacher_name',sa.String(),nullable=False),
        sa.Column('section',sa.String(),nullable=False),
        sa.Column('title',sa.String(),nullable=False),
        sa.Column('content',sa.String(),nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_table('teacher')
    pass
