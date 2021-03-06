"""Create account and role models.

Revision ID: e788b80d09eb
Revises: 
Create Date: 2017-06-18 17:50:27.361617

"""
import sqlalchemy as sa
from alembic import op

# Revision identifiers, used by Alembic.
revision = 'e788b80d09eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'role',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.Unicode(length=128), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'account',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('username', sa.Unicode(length=128), nullable=False),
        sa.Column('email', sa.Unicode(length=128), nullable=False),
        sa.Column('password', sa.Unicode(length=128), nullable=False),
        sa.Column('first_name', sa.Unicode(length=128), nullable=True),
        sa.Column('patr_name', sa.Unicode(length=128), nullable=True),
        sa.Column('last_name', sa.Unicode(length=128), nullable=True),
        sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account')
    op.drop_table('role')
    # ### end Alembic commands ###
