"""empty message

Revision ID: 364addb8e77e
Revises: 52cf88d0453f
Create Date: 2022-08-24 15:24:30.753147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '364addb8e77e'
down_revision = '52cf88d0453f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('livro', sa.Column('usuario_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'livro', 'usuario', ['usuario_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'livro', type_='foreignkey')
    op.drop_column('livro', 'usuario_id')
    # ### end Alembic commands ###