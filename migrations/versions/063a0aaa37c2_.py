"""empty message

Revision ID: 063a0aaa37c2
Revises: 8b348cb5fa6c
Create Date: 2022-09-15 21:43:55.747552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '063a0aaa37c2'
down_revision = '8b348cb5fa6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('orbit', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('orbit'),
    sa.UniqueConstraint('orbit')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    op.drop_table('people')
    # ### end Alembic commands ###
