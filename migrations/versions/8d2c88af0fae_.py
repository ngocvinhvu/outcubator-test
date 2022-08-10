"""empty message

Revision ID: 8d2c88af0fae
Revises: 
Create Date: 2022-08-10 14:21:57.324066

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "8d2c88af0fae"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "applicants",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column(
            "created_dttm",
            sa.DateTime(),
            server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
            nullable=True,
        ),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("dob", sa.DateTime(), nullable=True),
        sa.Column(
            "country",
            postgresql.ENUM(
                "VIETNAM",
                "SINGAPORE",
                "LAOS",
                "INDONESIA",
                "THAILAND",
                "CAMPUCHIA",
                "MALAYSIA",
                name="countries",
            ),
            nullable=True,
        ),
        sa.Column(
            "status",
            postgresql.ENUM("processed", "pending", "failed", name="status"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "results",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column(
            "created_dttm",
            sa.DateTime(),
            server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
            nullable=True,
        ),
        sa.Column(
            "status",
            postgresql.ENUM("processed", "pending", "failed", name="status"),
            nullable=True,
        ),
        sa.Column("applicant_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "processed_dttm",
            sa.DateTime(),
            server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["applicant_id"],
            ["applicants.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("results")
    op.drop_table("applicants")
    # ### end Alembic commands ###
