"""empty message

Revision ID: 5e3f7b11810d
Revises: 8d2c88af0fae
Create Date: 2022-08-10 16:46:27.104093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5e3f7b11810d"
down_revision = "8d2c88af0fae"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("results", sa.Column("client_key", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("results", "client_key")
    # ### end Alembic commands ###
