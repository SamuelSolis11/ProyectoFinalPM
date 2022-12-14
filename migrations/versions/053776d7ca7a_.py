"""empty message

Revision ID: 053776d7ca7a
Revises: 1e6d4c91c68b
Create Date: 2022-11-23 09:26:49.941072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '053776d7ca7a'
down_revision = '1e6d4c91c68b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('producto',
    sa.Column('idProducto', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombreProducto', sa.String(length=250), nullable=True),
    sa.Column('desProducto', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('idProducto')
    )
    op.create_table('proveedor',
    sa.Column('idProveedor', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombreProveedor', sa.String(length=250), nullable=True),
    sa.Column('direccion', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('idProveedor')
    )
    op.create_table('usuarios',
    sa.Column('idUsuario', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombreUsuario', sa.String(length=250), nullable=True),
    sa.Column('correo', sa.String(length=250), nullable=False),
    sa.Column('contraseña', sa.String(length=250), nullable=False),
    sa.Column('edad', sa.Integer(), nullable=True),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('idUsuario'),
    sa.UniqueConstraint('correo')
    )
    op.create_table('ventas',
    sa.Column('idVenta', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('fecha', sa.DateTime(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('idVenta')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ventas')
    op.drop_table('usuarios')
    op.drop_table('proveedor')
    op.drop_table('producto')
    # ### end Alembic commands ###
