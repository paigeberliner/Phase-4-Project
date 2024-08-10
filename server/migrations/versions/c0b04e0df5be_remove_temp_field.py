"""remove temp field

Revision ID: c0b04e0df5be
Revises: 606226d963db
Create Date: 2024-08-10 14:04:05.492088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0b04e0df5be'
down_revision = '606226d963db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('available_classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_name', sa.String(), nullable=True),
    sa.Column('studio', sa.String(), nullable=True),
    sa.Column('class_time', sa.DateTime(), nullable=True),
    sa.Column('class_duration', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_available_classes_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('claimed_classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('available_class_id', sa.Integer(), nullable=True),
    sa.Column('claimed_time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['available_class_id'], ['available_classes.id'], name=op.f('fk_claimed_classes_available_class_id_available_classes')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_claimed_classes_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('claimed_classes')
    op.drop_table('available_classes')
    op.drop_table('users')
    # ### end Alembic commands ###
