"""empty message

Revision ID: 49255a3bf8a4
Revises: b04ad51960d8
Create Date: 2021-01-27 13:51:36.909498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49255a3bf8a4'
down_revision = 'b04ad51960d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('TempClifor',
    sa.Column('cd_clifor', sa.Integer(), nullable=False),
    sa.Column('nr_fone', sa.String(length=11), nullable=True),
    sa.Column('nm_razao', sa.String(length=100), nullable=False),
    sa.Column('nm_endereco', sa.String(length=100), nullable=True),
    sa.Column('nr_endereco', sa.String(length=10), nullable=True),
    sa.Column('nm_bairro', sa.String(length=80), nullable=True),
    sa.Column('nr_cep', sa.String(length=8), nullable=True),
    sa.Column('nm_cidade', sa.String(length=100), nullable=True),
    sa.Column('nm_uf', sa.String(length=2), nullable=True),
    sa.Column('nm_fantasia', sa.String(length=100), nullable=True),
    sa.Column('nr_ie', sa.String(length=15), nullable=True),
    sa.Column('dt_altera', sa.Date(), nullable=True),
    sa.Column('nr_cpfcnpj', sa.String(length=14), nullable=False),
    sa.PrimaryKeyConstraint('cd_clifor')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TempClifor')
    # ### end Alembic commands ###
