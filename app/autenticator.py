from functools import wraps
import jwt
from flask import request, jsonify, current_app

from .model import Pessoa


def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None
        if 'autorization' in request.headers:
            token = request.headers['autorization']

        if not token:
            return jsonify({"erro": "não autorizado"}), 403

        if "Bearer" not in token:
            return jsonify({"erro": "token inválido"})

        try:
            token_pure = token.replace("Bearer", "")
            decode = jwt.decode(token_pure, current_app.config['SECRET_KEY'],
                                algorithms=['HS256'])

        except:
            return jsonify({'erro': 'token Inválido'})

        return f(*args, **kwargs)

    return wrapper
