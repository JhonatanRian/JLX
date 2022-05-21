"""remove size

Revision ID: 399d3c167b3c
Revises: b8b4aac88bd6
Create Date: 2022-05-21 08:27:08.211119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '399d3c167b3c'
down_revision = 'b8b4aac88bd6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_column('size')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('size', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###