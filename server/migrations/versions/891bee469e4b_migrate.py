"""Migrate

Revision ID: 891bee469e4b
Revises: acc126c77a63
Create Date: 2024-08-11 14:55:10.531917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '891bee469e4b'
down_revision = 'acc126c77a63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workoutclasses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('studio_name', sa.String(), nullable=True),
    sa.Column('studio_location', sa.String(), nullable=True),
    sa.Column('class_name', sa.String(), nullable=True),
    sa.Column('class_duration', sa.Integer(), nullable=True),
    sa.Column('class_date', sa.DateTime(), nullable=True),
    sa.Column('class_time', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('workout_classes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workout_classes',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('studio_name', sa.VARCHAR(), nullable=True),
    sa.Column('studio_location', sa.VARCHAR(), nullable=True),
    sa.Column('class_name', sa.VARCHAR(), nullable=True),
    sa.Column('class_duration', sa.INTEGER(), nullable=True),
    sa.Column('class_date', sa.DATETIME(), nullable=True),
    sa.Column('class_time', sa.DATETIME(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('workoutclasses')
    # ### end Alembic commands ###
