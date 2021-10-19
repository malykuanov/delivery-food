"""empty message

Revision ID: 3c9bd9e651b4
Revises: 1adec5604d61
Create Date: 2021-10-19 21:53:58.759104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c9bd9e651b4'
down_revision = '1adec5604d61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assoc_cart_products',
    sa.Column('cart_product_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cart_product_id'], ['cart_product.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], )
    )
    op.drop_constraint('product_cart_id_fkey', 'product', type_='foreignkey')
    op.drop_column('product', 'cart_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('cart_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('product_cart_id_fkey', 'product', 'cart_product', ['cart_id'], ['id'])
    op.drop_table('assoc_cart_products')
    # ### end Alembic commands ###
