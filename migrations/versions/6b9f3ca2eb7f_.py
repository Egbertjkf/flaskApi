"""empty message

Revision ID: 6b9f3ca2eb7f
Revises: 
Create Date: 2021-02-11 08:36:07.000573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b9f3ca2eb7f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Clifor',
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
    op.create_table('CondPg',
    sa.Column('cd_condpg', sa.Integer(), nullable=False),
    sa.Column('ds_condpg', sa.String(length=30), nullable=False),
    sa.Column('nr_parcelas', sa.Integer(), nullable=True),
    sa.Column('nr_diaspri', sa.Integer(), nullable=True),
    sa.Column('nr_intervalo', sa.Integer(), nullable=True),
    sa.Column('nr_dias1', sa.Integer(), nullable=True),
    sa.Column('nr_dias2', sa.Integer(), nullable=True),
    sa.Column('nr_dias3', sa.Integer(), nullable=True),
    sa.Column('nr_dias4', sa.Integer(), nullable=True),
    sa.Column('nr_dias5', sa.Integer(), nullable=True),
    sa.Column('nr_dias6', sa.Integer(), nullable=True),
    sa.Column('nr_dias7', sa.Integer(), nullable=True),
    sa.Column('nr_dias8', sa.Integer(), nullable=True),
    sa.Column('nr_dias9', sa.Integer(), nullable=True),
    sa.Column('nr_dias10', sa.Integer(), nullable=True),
    sa.Column('nr_fatorfin', sa.String(length=10), nullable=True),
    sa.Column('fl_status', sa.String(length=1), nullable=True),
    sa.Column('fl_tipo', sa.String(length=1), nullable=True),
    sa.PrimaryKeyConstraint('cd_condpg')
    )
    op.create_table('Pessoa',
    sa.Column('nr_idpessoa', sa.Integer(), nullable=False),
    sa.Column('nm_pessoa', sa.String(length=100), nullable=True),
    sa.Column('nm_apelido', sa.String(length=30), nullable=True),
    sa.Column('dt_nascimento', sa.String(length=10), nullable=True),
    sa.Column('fl_status', sa.String(length=1), nullable=True),
    sa.Column('ds_email', sa.String(length=100), nullable=True),
    sa.Column('nr_celular', sa.String(length=20), nullable=True),
    sa.Column('nr_idperfil', sa.Integer(), nullable=True),
    sa.Column('nm_senha', sa.String(length=10), nullable=True),
    sa.Column('vl_limiteordcom', sa.String(length=12), nullable=True),
    sa.Column('vl_limitepedven', sa.String(length=12), nullable=True),
    sa.Column('vl_limitefin', sa.String(length=12), nullable=True),
    sa.PrimaryKeyConstraint('nr_idpessoa')
    )
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
    sa.Column('nr_cpfcnpj', sa.String(length=14), nullable=False),
    sa.Column('cd_vendedor', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('cd_clifor', 'cd_vendedor')
    )
    op.create_table('pedido',
    sa.Column('nr_pedido', sa.Integer(), nullable=False),
    sa.Column('vl_pedido', sa.String(length=10), nullable=True),
    sa.Column('cd_clifor', sa.Integer(), nullable=False),
    sa.Column('dt_emissao', sa.Date(), nullable=False),
    sa.Column('vl_fator', sa.Integer(), nullable=False),
    sa.Column('cd_filial', sa.Integer(), nullable=False),
    sa.Column('cd_condpg', sa.Integer(), nullable=True),
    sa.Column('cd_vendedor', sa.Integer(), nullable=True),
    sa.Column('ds_observ', sa.String(length=250), nullable=True),
    sa.Column('fl_status', sa.String(length=1), nullable=True),
    sa.PrimaryKeyConstraint('nr_pedido')
    )
    op.create_table('produto',
    sa.Column('cd_produto', sa.Integer(), nullable=False),
    sa.Column('ds_produto', sa.String(length=100), nullable=True),
    sa.Column('vl_preco_venda', sa.String(length=10), nullable=True),
    sa.Column('cd_unidade', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('cd_produto')
    )
    op.create_table('tabpre_cli',
    sa.Column('cd_clifor', sa.Integer(), nullable=False),
    sa.Column('nr_sequen', sa.Integer(), nullable=False),
    sa.Column('cd_produto', sa.String(length=30), nullable=True),
    sa.Column('dt_implanta', sa.Date(), nullable=True),
    sa.Column('vl_tabela', sa.String(length=23), nullable=True),
    sa.Column('fl_status', sa.String(length=1), nullable=True),
    sa.Column('dt_ultvenda', sa.Date(), nullable=True),
    sa.Column('vl_percmax', sa.String(length=10), nullable=True),
    sa.Column('vl_percmin', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('cd_clifor', 'nr_sequen')
    )
    op.create_table('vendedor',
    sa.Column('cd_vendedor', sa.Integer(), nullable=False),
    sa.Column('nm_vendedor', sa.String(length=60), nullable=True),
    sa.Column('ds_senha', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('cd_vendedor')
    )
    op.create_table('it_pedido',
    sa.Column('nr_pedido', sa.Integer(), nullable=True),
    sa.Column('nr_sequen', sa.Integer(), nullable=False),
    sa.Column('nr_pedidoSist', sa.Integer(), nullable=True),
    sa.Column('cd_produto', sa.String(length=20), nullable=True),
    sa.Column('ds_complementar', sa.String(length=250), nullable=True),
    sa.Column('cd_unidade', sa.Integer(), nullable=True),
    sa.Column('qt_item', sa.String(length=23), nullable=True),
    sa.Column('vl_unit', sa.String(length=23), nullable=True),
    sa.Column('vl_percdesc', sa.String(length=3), nullable=True),
    sa.Column('vl_liquido', sa.String(length=30), nullable=True),
    sa.Column('ds_produto', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['nr_pedido'], ['pedido.nr_pedido'], ),
    sa.PrimaryKeyConstraint('nr_sequen')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('it_pedido')
    op.drop_table('vendedor')
    op.drop_table('tabpre_cli')
    op.drop_table('produto')
    op.drop_table('pedido')
    op.drop_table('TempClifor')
    op.drop_table('Pessoa')
    op.drop_table('CondPg')
    op.drop_table('Clifor')
    # ### end Alembic commands ###