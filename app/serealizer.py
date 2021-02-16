
from flask_marshmallow import Marshmallow


ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class PessoaSchema(ma.Schema):
    class Meta:
        fields = (
            "nr_idpessoa",
            "nm_pessoa",
            "nm_apelido",
            "dt_nascimento",
            "fl_status",
            "ds_email",
            "nr_celular",
            "nr_idperfil",
            "nm_senha",
            "vl_limiteordcom",
            "vl_limitepedven",
            "vl_limitefin"
        )


class CliforSchema(ma.Schema):
    class Meta:
        fields = (
            "cd_clifor",
            "nr_fone",
            "nm_razao",
            "nm_endereco",
            "nr_endereco",
            "nm_bairro",
            "nr_cep",
            "nm_cidade",
            "nm_uf",
            "nm_fantasia",
            "nr_ie",
            "dt_altera",
            "nr_cpfcnpj",
            "cd_classif"

        )


class TempCliforSchema(ma.Schema):
    class Meta:
        fields = (
            "cd_clifor",
            "nr_fone",
            "nm_razao",
            "nm_endereco",
            "nr_endereco",
            "nm_bairro",
            "nr_cep",
            "nm_cidade",
            "nm_uf",
            "nm_fantasia",
            "dt_altera",
            "nr_cpfcnpj",
            "cd_vendedor"

        )


class CondPgSchema(ma.Schema):
    class Meta:
        fields = (
            "cd_condpg",
            "ds_condpg",
            "nr_parcelas",
            "nr_diaspri",
            "nr_intervalo",
            "nr_dias1",
            "nr_dias2",
            "nr_dias3",
            "nr_dias4",
            "nr_dias5",
            "nr_dias6",
            "nr_dias7",
            "nr_dias8",
            "nr_dias9",
            "nr_dias10",
            "nr_fatorfin",
            "fl_status",
            "fl_tipo"
        )


class ItPedidoSchema(ma.Schema):
    class Meta:
        fields = (
            "nr_pedido",
            "nr_sequen",
            "nr_pedidoSist",
            "cd_produto",
            "ds_complementar",
            "cd_unidade",
            "qt_item",
            "vl_unit",
            "vl_percdesc",
            "vl_liquido",
            "ds_produto"
        )


class ProdutoSchema(ma.Schema):
    class Meta:
        fields = (
            "cd_produto",
            "ds_produto",
            "vl_preco_venda",
            "cd_unidade"
        )


class Tabpre_cliSchema(ma.Schema):
    class Meta:
        fields = (
            "cd_clifor",
            "ds_produto",
            "nr_sequen",
            "dt_implanta",
            "vl_tabela",
            "fl_status",
            "dt_ultvenda",
            "vl_percmax",
            "vl_percmin",
            "cd_produto"
        )


class VendedorSchema(ma.Schema):
    class Meta:
        fields = (
            "cd_vendedor",
            "nm_vendedor",
        )


class PedidoSchema(ma.Schema):
    class Meta:
        fields = (
            "nr_pedido",
            "vl_pedido",
            "cd_clifor",
            "dt_emissao",
            "vl_fator",
            "cd_filial",
            "cd_condpg",
            "cd_vendedor",
            "ds_observ",
            "fl_status"
        )
