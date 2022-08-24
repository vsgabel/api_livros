"""empty message

Revision ID: 805591eb739d
Revises: 364addb8e77e
Create Date: 2022-08-24 15:38:03.101457

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '805591eb739d'
down_revision = '364addb8e77e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('livro', sa.Column('autor', sa.String(length=32), nullable=False))
    op.alter_column('livro', 'usuario_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('livro', 'usuario_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.drop_column('livro', 'autor')
    # ### end Alembic commands ###
