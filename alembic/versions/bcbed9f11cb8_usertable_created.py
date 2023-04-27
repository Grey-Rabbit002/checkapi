"""userTable Created

Revision ID: bcbed9f11cb8
Revises: 5c5b81202800
Create Date: 2023-04-27 15:08:01.986017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcbed9f11cb8'
down_revision = '5c5b81202800'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
        sa.Column('dept_id',sa.Integer(),nullable=False),
        sa.Column('username',sa.String(),nullable=False),
        sa.Column('email',sa.String(),nullable=False),
        sa.Column('password',sa.String(),nullable=False),)
def downgrade() -> None:
    op.drop_table('user')
