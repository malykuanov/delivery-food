"""empty message

Revision ID: a76cd4740049
Revises: a78e4b3140d4
Create Date: 2021-10-13 21:59:07.252140

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'a76cd4740049'
down_revision = 'a78e4b3140d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('photo_url', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'photo_url')
    # ### end Alembic commands ###
