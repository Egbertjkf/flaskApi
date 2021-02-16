
from .autenticator import jwt_required
from flask import Blueprint, request
from .model import (Pessoa, db, Clifor, CondPg, It_pedido, Produto,
                    Tabpre_cli, Vendedor, Pedido, TempClifor)
from .serealizer import (PessoaSchema, CliforSchema, CondPgSchema,
                         ItPedidoSchema, PedidoSchema, ProdutoSchema,
                         Tabpre_cliSchema, VendedorSchema)

bp_pessoa = Blueprint('Pessoa', __name__)
bp_clifor = Blueprint('Clifor', __name__)
bp_condpg = Blueprint('CondPg', __name__)
bp_itpedido = Blueprint('It_pedido', __name__)
bp_pedido = Blueprint('Pedido', __name__)
bp_produto = Blueprint('Produto', __name__)
bp_tabpre_cli = Blueprint('Tabpre_cli', __name__)
bp_vendedor = Blueprint('Vendedor', __name__)
bp_Tempclifor = Blueprint('TempClifor', __name__)


@bp_vendedor.route('/impVendedor',methods=['GET'])
@jwt_required
def mostraVendedor():
    vs = VendedorSchema(many=True)
    result = Vendedor.query.all()
    return vs.jsonify(result)

@bp_vendedor.route('/CadVendedor',methods=['POST'])
@jwt_required
def CadVendedor():
    if request.is_json:
        data = request.get_json()
        if type(data) == list:
            itens = len(data)
            s = 0
            while s <= itens-1:
                lista = data[s]
                new_Vendedor = Vendedor(
                    cd_clifor=lista['cd_vendedor'],
                    nr_fone=lista['nm_vendedor']
                    )
                db.session.add(new_Vendedor)
                db.session.commit()
                s = s + 1
            return {"status": "Enviado"}
    else:
        return {"error": "The request payload is not in JSON format"}
 



@bp_pessoa.route('/impPessoa', methods=['GET'])
@jwt_required
def mostrar():
    ps = PessoaSchema(many=True)
    result = Pessoa.query.all()
    return ps.jsonify(result)


@bp_pessoa.route('/cadPessoa', methods=['POST'])
@jwt_required
def cadastrar():
    if request.is_json:
        data = request.get_json()
        if type(data) == list:
            itens = len(data)
            s = 0
            while s <= itens-1:
                lista = data[s]
                new_pessoa = Pessoa(
                    nr_idpessoa=lista['nr_idpessoa'],
                    nm_pessoa=lista['nm_pessoa'],
                    nm_apelido=lista['nm_apelido'],
                    dt_nascimento=lista['dt_nascimento'],
                    fl_status=lista['fl_status'],
                    ds_email=lista['ds_email'],
                    nr_celular=lista['nr_celular'],
                    nr_idperfil=lista['nr_idperfil'],
                    nm_senha=lista['nm_senha'],
                    vl_limiteordcom=lista['vl_limiteordcom'],
                    vl_limitepedven=lista['vl_limitepedven'],
                    vl_limitefin=lista['vl_limitefin']
                )
                s = s + 1
                db.session.add(new_pessoa)
            db.session.commit()
        return {"status": "Enviado"}
    else:
        return {"error": "The request payload is not in JSON format"}


@bp_clifor.route('/impClifor', methods=['GET'])
@jwt_required
def mostraClifor():
    cs = CliforSchema(many=True)
    if 'dataimp' in request.headers:
        dataimp = request.headers['dataimp']
        result = Clifor.query.filter(Clifor.dt_altera >= dataimp)
    else:
        dataimp = ''
        result = Clifor.query.all()
    return cs.jsonify(result)


@bp_clifor.route('/CadClifor', methods=['POST'])
@jwt_required
def cadastraClifor():
    if request.is_json:
        data = request.get_json()
        if type(data) == list:
            itens = len(data)
            s = 0
            while s <= itens-1:
                lista = data[s]
                new_clifor = Clifor(
                    cd_clifor=lista['cd_clifor'],
                    nr_fone=lista['nr_fone'],
                    nm_razao=lista['nm_razao'],
                    nm_endereco=lista['nm_endereco'],
                    nr_endereco=lista['nr_endereco'],
                    nm_bairro=lista['nm_bairro'],
                    nr_cep=lista['nr_cep'],
                    nm_cidade=lista['nm_cidade'],
                    nm_uf=lista['nm_uf'],
                    nm_fantasia=lista['nm_fantasia'],
                    nr_cpfcnpj=lista['nr_cpfcnpj'],
                    cd_vendedor=lista['cd_vendedor'],
                    cd_classif=lista['cd_classif'],
                    dt_altera = lista['dt_altera']
                )
                db.session.add(new_clifor)
                db.session.commit()
                s = s + 1
            return {"status": "Enviado"}
        else:
            new_clifor = Clifor(
                cd_clifor=data['cd_clifor'],
                nr_fone=data['nr_fone'],
                nm_razao=data['nm_razao'],
                nm_endereco=data['nm_endereco'],
                nr_endereco=data['nr_endereco'],
                nm_bairro=data['nm_bairro'],
                nr_cep=data['nr_cep'],
                nm_cidade=data['nm_cidade'],
                nm_uf=data['nm_uf'],
                nm_fantasia=data['nm_fantasia'],
                nr_ie=data['nr_ie'],
                nr_cpfcnpj=data['nr_cpfcnpj'],
                cd_vendedor=data['cd_vendedor'],
                cd_classif=lista['cd_classif']
            )
            db.session.add(new_clifor)
            db.session.commit()
            return {"status": "Enviado"}
    else:
        return {"error": "The request payload is not in JSON format"}, 401


@bp_Tempclifor.route('/impTempClifor', methods=['GET'])
@jwt_required
def mostraCondPg():
    ctps = TempCliforSchema(many=True)
    result = TempClifor.query.all()
    return ctps.jsonify(result)

@bp_Tempclifor.route('/cadTempClifor', methods=['POST'])
@jwt_required
def cadastraTempClifor():
    if request.is_json:
        data = request.get_json()
        if type(data) == list:
            itens = len(data)
            s = 0
            while s <= itens-1:
                lista = data[s]
                new_clifor = TempClifor(
                    cd_clifor=lista['cd_clifor'],
                    nr_fone=lista['nr_fone'],
                    nm_razao=lista['nm_razao'],
                    nm_endereco=lista['nm_endereco'],
                    nr_endereco=lista['nr_endereco'],
                    nm_bairro=lista['nm_bairro'],
                    nr_cep=lista['nr_cep'],
                    nm_cidade=lista['nm_cidade'],
                    nm_uf=lista['nm_uf'],
                    nm_fantasia=lista['nm_fantasia'],
                    nr_ie=lista['nr_ie'],
                    nr_cpfcnpj=lista['nr_cpfcnpj'],
                    cd_vendedor=lista['cd_vendedor']
                )
                db.session.add(new_clifor)
                db.session.commit()
                s = s + 1
            return {"status": "Enviado"}
        else:
            new_clifor = TempClifor(
                cd_clifor=data['cd_clifor'],
                nr_fone=data['nr_fone'],
                nm_razao=data['nm_razao'],
                nm_endereco=data['nm_endereco'],
                nr_endereco=data['nr_endereco'],
                nm_bairro=data['nm_bairro'],
                nr_cep=data['nr_cep'],
                nm_cidade=data['nm_cidade'],
                nm_uf=data['nm_uf'],
                nm_fantasia=data['nm_fantasia'],
                nr_ie=data['nr_ie'],
                nr_cpfcnpj=data['nr_cpfcnpj'],
                cd_vendedor=data['cd_vendedor']
            )
            db.session.add(new_clifor)
            db.session.commit()
            return {"status": "Enviado"}
    else:
        return {"error": "The request payload is not in JSON format"}, 401


@bp_condpg.route('/impCondPg', methods=['GET'])
@jwt_required
def mostraCondPg():
    cpgs = CondPgSchema(many=True)
    result = CondPg.query.all()
    return cpgs.jsonify(result)


"""
@bp_condpg.route('/cadCondPg', methods=['POST'])
def cadastraCondPg()
"""


@bp_itpedido.route('/impItpedido', methods=['GET'])
@jwt_required
def mostraItPedido():
    itps = ItPedidoSchema(many=True)
    result = It_pedido.query.all()
    return itps.jsonify(result)


@bp_itpedido.route('/cadItpedido', methods=['POST'])
@jwt_required
def cadastraItPedido():
    if request.is_json:
        data = request.get_json()
        new_itpedido = It_pedido(
            nr_pedido=data["nr_pedido"],
            nr_sequen=data["nr_sequen"],
            nr_pedidoSist=data["nr_pedidoSist"],
            cd_produto=data["cd_produto"],
            ds_complementar=data["ds_complementar"],
            cd_unidade=data["cd_unidade"],
            qt_item=data["qt_item"],
            vl_unit=data["vl_unit"],
            vl_percdesc=["vl_percdesc"],
            vl_liquido=data["vl_liquido"],
            ds_produto=data["ds_produto"]
        )
        db.session.add(new_itpedido)
        db.session.commit()
        return {"status": "Enviado"}
    else:
        return {"error": "The request payload is not in JSON format"}


@bp_pedido.route('/impPedido', methods=['GET'])
@jwt_required
def mostraPedido():
    peds = PedidoSchema(many=True)
    result = it_pedido.query.all()
    return peds.jsonify(result)


@bp_pedido.route('/cadPedido', methods=['POST'])
@jwt_required
def cadastraPedido():
    if request.is_json:
        data = request.get_json()
        itens = len(data)
        s = 0
        while s <= itens-1:
            lista = data[s]
            new_pedido = Pedido(
                nr_pedido=lista["nr_pedido"],
                vl_pedido=lista["vl_pedido"],
                cd_clifor=lista["cd_clifor"],
                dt_emissao=lista["dt_emissao"],
                vl_fator=lista["vl_fator"],
                cd_filial=lista["cd_filial"],
                cd_condpg=lista["cd_condpg"],
                cd_vendedor=lista["cd_vendedor"],
                ds_observ=lista["ds_observ"],
                fl_status=lista["fl_status"]
            )
            dataIT = lista['itens']
            n = 0
            itensIt = len(dataIT)
            while n <= itensIt-1:
                listaIt = dataIT[n]
                new_itpedido = It_pedido(
                    nr_pedido=listaIt["nr_pedido"],
                    nr_pedidoSist=listaIt["nr_pedidoSist"],
                    cd_produto=listaIt["cd_produto"],
                    ds_complementar=listaIt["ds_complementar"],
                    cd_unidade=listaIt["cd_unidade"],
                    qt_item=listaIt["qt_item"],
                    vl_unit=listaIt["vl_unit"],
                    vl_percdesc=listaIt["vl_percdesc"],
                    vl_liquido=listaIt["vl_liquido"],
                    ds_produto=listaIt["ds_produto"],
                    nr_sequen=listaIt["nr_sequen"]
                )
                n = n+1
                db.session.add(new_itpedido)
            s = s + 1
            db.session.add(new_pedido)
        db.session.commit()
        return {"status": "Enviado"}
    else:
        return {"error": "The request payload is not in JSON format"}


@bp_produto.route('/impProduto', methods=['GET'])
@jwt_required
def mostraProd():
    prods = ProdutoSchema(many=True)
    result = Produto.query.all()
    return prods.jsonify(result)


@bp_tabpre_cli.route('/impTabPreCli', methods=['GET'])
@jwt_required
def mostraTabPreCli():
    tabpres = Tabpre_cliSchema(many=True)
    if 'dataimp' in request.headers:
        dataimp = request.headers['dataimp']
        result = Tabpre_cli.query.filter(Tabpre_cli.dt_altera >= dataimp)
    else:
        dataimp = ''
        result = Tabpre_cli.query.all()
    return tabpres.jsonify(result)


@bp_tabpre_cli.route('/CadTabPreCli', methods=['POST'])
@jwt_required
def cadastraTabPreCli():
    if request.is_json:
        data = request.get_json()
        if type(data) == list:
            itens = len(data)
            s = 0
            while s <= itens-1:
                lista = data[s]
                new_clifor = Tabpre_cli(
                    cd_clifor=lista['cd_clifor'],
                    cd_produto=lista['cd_produto'],
                    ds_produto=lista['ds_produto'],
                    nr_sequen=lista['nr_sequen'],
                    dt_implanta=lista['dt_implanta'],
                    vl_tabela=lista['vl_tabela'],
                    fl_status=lista['fl_status'],
                    vl_descmax=lista['vl_descmax'],
                    vl_acremax=lista['vl_acremax']
                )
                db.session.add(new_clifor)
                try:
                    db.session.commit()
                except:
                    pass
                s = s + 1
            return {"status": "Enviado"}


@bp_pessoa.route('/internet', methods=['GET'])
@jwt_required
def testeInt():
    return {"internet": "True"}
