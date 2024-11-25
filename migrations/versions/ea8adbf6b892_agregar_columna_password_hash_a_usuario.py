"""Agregar columna password_hash a usuario

Revision ID: ea8adbf6b892
Revises: 
Create Date: 2024-11-24 20:09:04.092054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea8adbf6b892'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(length=128), nullable=False))
        batch_op.drop_column('telefono')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('telefono', sa.VARCHAR(length=15), nullable=False))
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###
