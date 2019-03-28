"""add mobile

Revision ID: 93a4e39444e6
Revises: 6209041af3d5
Create Date: 2019-03-28 18:16:50.469000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93a4e39444e6'
down_revision = '6209041af3d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_authors', sa.Column('mobile', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tbl_authors', 'mobile')
    # ### end Alembic commands ###