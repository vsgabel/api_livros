"""empty message

Revision ID: b8b60cf2b3d7
Revises: b951fc21a078
Create Date: 2022-08-24 15:41:29.942234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8b60cf2b3d7'
down_revision = 'b951fc21a078'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('livro', sa.Column('nome', sa.String(length=64), nullable=False))
    op.add_column('livro', sa.Column('autor', sa.String(length=64), nullable=False))
    op.add_column('livro', sa.Column('editora', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('livro', 'editora')
    op.drop_column('livro', 'autor')
    op.drop_column('livro', 'nome')
    # ### end Alembic commands ###
