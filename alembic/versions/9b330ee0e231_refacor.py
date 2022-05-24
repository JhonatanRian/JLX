"""refacor

Revision ID: 9b330ee0e231
Revises: 1c5e3cd32c02
Create Date: 2022-05-24 08:01:47.271780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b330ee0e231'
down_revision = '1c5e3cd32c02'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('request', schema=None) as batch_op:
        batch_op.drop_constraint('fk_product', type_='foreignkey')
        batch_op.create_foreign_key('fk_product', 'product', ['product_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('request', schema=None) as batch_op:
        batch_op.drop_constraint('fk_product', type_='foreignkey')
        batch_op.create_foreign_key('fk_product', 'user', ['product_id'], ['id'])

    # ### end Alembic commands ###
