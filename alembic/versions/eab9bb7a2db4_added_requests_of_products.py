"""added requests of products

Revision ID: eab9bb7a2db4
Revises: 3a125320e129
Create Date: 2022-05-22 06:16:30.973638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eab9bb7a2db4'
down_revision = '3a125320e129'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('request', schema=None) as batch_op:
        batch_op.add_column(sa.Column('observation', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('request', schema=None) as batch_op:
        batch_op.drop_column('observation')

    # ### end Alembic commands ###
