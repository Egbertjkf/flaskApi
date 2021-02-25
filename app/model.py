from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class Pessoa(db.Model):

    __tablename__ = 'Pessoa'

    nr_idpessoa = db.Column(db.Integer, primary_key=True)
    nm_pessoa = db.Column(db.String(100))
    nm_apelido = db.Column(db.String(30))
    dt_nascimento = db.Column(db.String(10))
    fl_status = db.Column(db.String(1))
    ds_email = db.Column(db.String(100))
    nr_celular = db.Column(db.String(20))
    nr_idperfil = db.Column(db.Integer)
    nm_senha = db.Column(db.String(10))
    vl_limiteordcom = db.Column(db.String(12))
    vl_limitepedven = db.Column(db.String(12))
    vl_limitefin = db.Column(db.String(12))

    def __init__(self, nr_idpessoa, nm_pessoa, nm_apelido,
                 dt_nascimento,  fl_status, ds_email, nr_celular,
                 nr_idperfil, nm_senha, vl_limiteordcom,
                 vl_limitepedven, vl_limitefin):
        self.nr_idpessoa = nr_idpessoa
        self.nm_pessoa = nm_pessoa
        self.nm_apelido = nm_apelido
        self.dt_nascimento = dt_nascimento
        self.fl_status = fl_status
        self.ds_email = ds_email
        self.nr_celular = nr_celular
        self.nr_idperfil = nr_idperfil
        self.nm_senha = nm_senha
        self.vl_limiteordcom = vl_limiteordcom
        self.vl_limitepedven = vl_limitepedven
        self.vl_limitefin = vl_limitefin

    def __repr__(self):
        return f"< Pessoa {self.nm_pessoa} >"


class Clifor(db.Model):

    __tablename__ = 'Clifor'

    cd_clifor = db.Column(db.Integer, primary_key=True)
    nr_fone = db.Column(db.String(11))
    nm_razao = db.Column(db.String(100), nullable=False)
    nm_endereco = db.Column(db.String(100))
    nr_endereco = db.Column(db.String(10))
    nm_bairro = db.Column(db.String(80))
    nr_cep = db.Column(db.String(8))
    nm_cidade = db.Column(db.String(100))
    nm_uf = db.Column(db.String(2))
    nm_fantasia = db.Column(db.String(100))
    nr_ie = db.Column(db.String(15))
    dt_altera = db.Column(db.Date)
    nr_cpfcnpj = db.Column(db.String(14), nullable=False)
    cd_classif = db.Column(db.Integer)
    cd_vendedor= db.Column(db.Integer,nullable=False)

    def __init__(self, cd_clifor, nr_fone, nm_razao, nm_endereco, nr_endereco, nm_bairro,
                 nr_cep, nm_cidade, nm_uf, nm_fantasia, nr_cpfcnpj, dt_altera,cd_classif,cd_vendedor):
        self.cd_clifor = cd_clifor
        self.nr_fone = nr_fone
        self.nm_razao = nm_razao
        self.nm_endereco = nm_endereco
        self.nr_endereco = nr_endereco
        self.nm_bairro = nm_bairro
        self.nr_cep = nr_cep
        self.nm_cidade = nm_cidade
        self.nm_uf = nm_uf
        self.nm_fantasia = nm_fantasia
        self.dt_altera = dt_altera
        self.nr_cpfcnpj = nr_cpfcnpj
        self.cd_classif = cd_classif
        self.cd_vendedor = cd_vendedor

    def __repr__(self):
        return f"< Clifor {self.nm_fantasia} >"


class TempClifor(db.Model):

    __tablename__ = 'TempClifor'

    cd_clifor = db.Column(db.Integer, primary_key=True)
    nr_fone = db.Column(db.String(11))
    nm_razao = db.Column(db.String(100), nullable=False)
    nm_endereco = db.Column(db.String(100))
    nr_endereco = db.Column(db.String(10))
    nm_bairro = db.Column(db.String(80))
    nr_cep = db.Column(db.String(8))
    nm_cidade = db.Column(db.String(100))
    nm_uf = db.Column(db.String(2))
    nm_fantasia = db.Column(db.String(100))
    nr_ie = db.Column(db.String(15))
    nr_cpfcnpj = db.Column(db.String(14), nullable=False)
    cd_vendedor = db.Column(db.Integer, primary_key=True)

    def __init__(self, cd_clifor, nr_fone, nm_razao, nm_endereco, nr_endereco, nm_bairro,
                 nr_cep, nm_cidade, nm_uf, nm_fantasia, nr_ie, nr_cpfcnpj, cd_vendedor):
        self.cd_clifor = cd_clifor
        self.nr_fone = nr_fone
        self.nm_razao = nm_razao
        self.nm_endereco = nm_endereco
        self.nr_endereco = nr_endereco
        self.nm_bairro = nm_bairro
        self.nr_cep = nr_cep
        self.nm_cidade = nm_cidade
        self.nm_uf = nm_uf
        self.nm_fantasia = nm_fantasia
        self.nr_ie = nr_ie
        self.nr_cpfcnpj = nr_cpfcnpj
        self.cd_vendedor = cd_vendedor

    def __repr__(self):
        return f"< Clifor {self.nm_fantasia} >"


class CondPg(db.Model):

    __tablename__ = 'CondPg'

    cd_condpg = db.Column(db.Integer, primary_key=True)
    ds_condpg = db.Column(db.String(30), nullable=False)
    nr_parcelas = db.Column(db.Integer)
    nr_diaspri = db.Column(db.Integer)
    nr_intervalo = db.Column(db.Integer)
    nr_dias1 = db.Column(db.Integer)
    nr_dias2 = db.Column(db.Integer)
    nr_dias3 = db.Column(db.Integer)
    nr_dias4 = db.Column(db.Integer)
    nr_dias5 = db.Column(db.Integer)
    nr_dias6 = db.Column(db.Integer)
    nr_dias7 = db.Column(db.Integer)
    nr_dias8 = db.Column(db.Integer)
    nr_dias9 = db.Column(db.Integer)
    nr_dias10 = db.Column(db.Integer)
    nr_fatorfin = db.Column(db.String(10))
    fl_status = db.Column(db.String(1))
    fl_tipo = db.Column(db.String(1))

    def __init__(self, cd_condpg, ds_condpg, nr_parcelas, nr_diaspri, nr_intervalo, nr_dias1,
                 nr_dias2, nr_dias3, nr_dias4, nr_dias5, nr_dias6, nr_dias7, nr_dias8, nr_dias9,
                 nr_dias10, nr_fatorfin, fl_status, fl_tipo):
        self.cd_condpg = cd_condpg
        self.ds_condpg = ds_condpg
        self.nr_parcelas = nr_parcelas
        self.nr_diaspri = nr_diaspri
        self.nr_intervalo = nr_intervalo
        self.nr_dias1 = nr_dias1
        self.nr_dias2 = nr_dias2
        self.nr_dias3 = nr_dias3
        self.nr_dias4 = nr_dias4
        self.nr_dias5 = nr_dias5
        self.nr_dias6 = nr_dias6
        self.nr_dias7 = nr_dias7
        self.nr_dias8 = nr_dias8
        self.nr_dias9 = nr_dias9
        self.nr_dias10 = nr_dias10
        self.nr_fatorfin = nr_fatorfin
        self.fl_status = fl_status
        self.fl_tipo = fl_tipo

    def __repr__(self):
        return f"< CondPg {self.ds_condpg} >"


class It_pedido(db.Model):

    __tablename__ = 'it_pedido'

    nr_pedido = db.Column(db.Integer, db.ForeignKey('pedido.nr_pedido'))
    nr_sequen = db.Column(db.Integer, primary_key=True)
    nr_pedidoSist = db.Column(db.Integer)
    cd_produto = db.Column(db.String(20))
    ds_complementar = db.Column(db.String(250))
    cd_unidade = db.Column(db.Integer)
    qt_item = db.Column(db.String(23))
    vl_unit = db.Column(db.String(23))
    vl_percdesc = db.Column(db.String(3))
    vl_liquido = db.Column(db.String(30))
    ds_produto = db.Column(db.String(100))

    def __init__(self, nr_pedido, nr_sequen, nr_pedidoSist, cd_produto, ds_complementar, cd_unidade,
                 qt_item, vl_unit, vl_percdesc, vl_liquido, ds_produto):
        self.nr_pedido = nr_pedido
        self.nr_sequen = nr_sequen
        self.nr_pedidoSist = nr_pedidoSist
        self.cd_produto = cd_produto
        self.ds_complementar = ds_complementar
        self.cd_unidade = cd_unidade
        self.qt_item = qt_item
        self.vl_unit = vl_unit
        self.vl_percdesc = vl_percdesc
        self.vl_liquido = vl_liquido
        self.ds_produto = ds_produto

    def __repr__(self):
        return f"< It_pedido {self.nr_pedido} >"


class Produto(db.Model):

    __tablename__ = "produto"

    cd_produto = db.Column(db.Integer, primary_key=True)
    ds_produto = db.Column(db.String(100))
    vl_preco_venda = db.Column(db.String(10))
    cd_unidade = db.Column(db.String(5))

    def __init__(self, cd_produto, ds_produto, vl_preco_venda, cd_unidade):
        self.cd_produto = cd_produto
        self.ds_produto = ds_produto
        self.vl_preco_venda = vl_preco_venda
        self.cd_unidade = cd_unidade

    def __repr__(self):
        return f"< Produto {self.cd_produto} >"


class Tabpre_cli(db.Model):

    __tablename__ = "tabpre_cli"

    cd_clifor = db.Column(db.Integer, primary_key=True)
    nr_sequen = db.Column(db.Integer, primary_key=True)
    cd_produto = db.Column(db.String(30))
    dt_implanta = db.Column(db.Date)
    vl_tabela = db.Column(db.String(23))
    fl_status = db.Column(db.String(1))
    vl_desccmax = db.Column(db.String(10))
    vl_acremax = db.Column(db.String(10))
    ds_produto = db.Column(db.String(100))

    def __init__(self, cd_clifor, nr_sequen, cd_produto, dt_implanta, vl_tabela, fl_status, vl_descmax, vl_acremax,ds_produto):
        self.cd_clifor = cd_clifor
        self.ds_produto = ds_produto
        self.nr_sequen = nr_sequen
        self.dt_implanta = dt_implanta
        self.vl_tabela = vl_tabela
        self.fl_status = fl_status
        self.vl_descmax = vl_descmax
        self.vl_acremax = vl_acremax
        self.cd_produto = cd_produto
        

    def __repr__(self):
        return f"< Clifor {self.cd_clifor} >"


class Vendedor(db.Model):

    __tablename__ = "vendedor"

    cd_vendedor = db.Column(db.Integer, primary_key=True)
    nm_vendedor = db.Column(db.String(60))

    def __init__(self, cd_vendedor, nm_vendedor):
        self.cd_vendedor = cd_vendedor
        self.nm_vendedor = nm_vendedor

    def __repr__(self):
        return f"< Vendedor {self.cd_vendedor} >"


class Pedido(db.Model):

    __tablename__ = "pedido"

    nr_pedido = db.Column(db.Integer, primary_key=True)
    vl_pedido = db.Column(db.String(10))
    cd_clifor = db.Column(db.Integer, nullable=False)
    dt_emissao = db.Column(db.Date, nullable=False)
    vl_fator = db.Column(db.Integer, nullable=False)
    cd_filial = db.Column(db.Integer, nullable=False)
    cd_condpg = db.Column(db.Integer)
    cd_vendedor = db.Column(db.Integer)
    ds_observ = db.Column(db.String(250))
    fl_status = db.Column(db.String(1))

    def __init__(self, nr_pedido, vl_pedido, cd_clifor, dt_emissao, vl_fator, cd_filial, cd_condpg,
                 cd_vendedor, ds_observ, fl_status):
        self.nr_pedido = nr_pedido
        self.vl_pedido = vl_pedido
        self.cd_clifor = cd_clifor
        self.dt_emissao = dt_emissao
        self.vl_fator = vl_fator
        self.cd_filial = cd_filial
        self.cd_condpg = cd_condpg
        self.cd_vendedor = cd_vendedor
        self.ds_observ = ds_observ
        self.fl_status = fl_status

    def __repr__(self):
        return f"< Pedido {self.nr_pedido} >"
