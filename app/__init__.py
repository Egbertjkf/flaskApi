
from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serealizer import configure as config_ma


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
 #   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sksistemas:d218fh27h@pgsql.sksistemas.com.br:5432/sksistemas'
 #   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#    app.config['SECRET_KEY'] = 'secret'

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from .rotas import bp_pessoa
    app.register_blueprint(bp_pessoa)

    from .rotas import bp_clifor
    app.register_blueprint(bp_clifor)

    from .rotas import bp_condpg
    app.register_blueprint(bp_condpg)

    from .rotas import bp_itpedido
    app.register_blueprint(bp_itpedido)

    from .rotas import bp_produto
    app.register_blueprint(bp_produto)

    from .rotas import bp_tabpre_cli
    app.register_blueprint(bp_tabpre_cli)

    from .rotas import bp_vendedor
    app.register_blueprint(bp_vendedor)

#    from .rotas import bp_vendedor
#    app.register_blueprint(bp_vendedor)

    from .rotas import bp_pedido
    app.register_blueprint(bp_pedido)

    from .rotas import bp_Tempclifor
    app.register_blueprint(bp_Tempclifor)


    return app
