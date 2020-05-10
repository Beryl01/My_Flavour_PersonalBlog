"""Initial migration

Revision ID: ebfc9f03bec8
Revises: 535ecccca644
Create Date: 2018-06-25 17:44:04.950239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebfc9f03bec8'
down_revision = '535ecccca644'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('description', sa.Text(), nullable=True))
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=False))
    op.drop_constraint('comments_owneer_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch_id'], ['id'])
    op.drop_column('comments', 'owneer_id')
    op.drop_column('comments', 'body')
    op.add_column('pitches', sa.Column('downvotes', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('upvotes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'upvotes')
    op.drop_column('pitches', 'downvotes')
    op.add_column('comments', sa.Column('body', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('owneer_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_owneer_id_fkey', 'comments', 'users', ['owneer_id'], ['id'])
    op.drop_column('comments', 'pitch_id')
    op.drop_column('comments', 'description')
    # ### end Alembic commands ###