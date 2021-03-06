"""empty message

Revision ID: 58303c6fd463
Revises: 052b72b2c5ce
Create Date: 2021-10-16 01:59:06.493346

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '58303c6fd463'
down_revision = '052b72b2c5ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('slug', sa.String(length=100), nullable=True))
    op.create_unique_constraint(None, 'product', ['slug'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product', type_='unique')
    op.drop_column('product', 'slug')
    # ### end Alembic commands ###
