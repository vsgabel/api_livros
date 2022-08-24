from config import Config
from app.serializer import Serializer
from functools import wraps
from flask import g, request, abort
from flask_httpauth import HTTPTokenAuth

token_auth =  HTTPTokenAuth()

@token_auth.verify_token
def verify_token(token):
    if token:
        try:
            u = Serializer.verify_auth_token(Config.SECRET_KEY, token.encode("utf-8"))
        except:
            return False
        if u:
            g.current_user = u
            return True
    return False

def campos_obrigatorios(campos, origem="JSON"):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if origem == "JSON":
                dados = request.get_json()
            elif origem == "URL":
                dados = request.args
            elif origem == "FORM":
                dados = request.form
            else:
                raise Exception("Esta origem de dados não é válida.")
            requisitos(campos, dados.keys())
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def requisitos(campos, chaves):
    falta = []

    for campo in campos:
        if campo not in chaves:
            falta.append(campo)        
    
    if falta:
        abort(422, f"O(s) campo(s) {falta} é(são) obrigatório(s)")