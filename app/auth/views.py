from flask import request, jsonify
from app import db
from app.auth import auth
from app.models import Usuario
from app.serializer import Serializer
from app.decorators import token_auth, campos_obrigatorios

@auth.route("/login", methods=['POST'])
@campos_obrigatorios(['email', 'senha'])
def login():
    data = request.get_json()
    
    email = data['email']
    senha = data['senha']

    u = Usuario.query.filter_by(email=email).first()
    if not u:
        return jsonify({"message": "Usuário não encontrado"}), 401

    status = u.verifica_senha(senha)
    if not status:
        return jsonify({"message": "Senha inválida"}), 401

    token = Serializer.generate_confirmation_token("froxilda", u.id, u.nome)
    return jsonify({"message": "Login efetuado com sucesso", "token": token}), 200

@auth.route("/registro", methods=['POST'])
@campos_obrigatorios(['nome', 'email', 'senha'])
def registro():
    data = request.get_json()
    
    nome = data['nome']
    email = data['email']
    senha = data['senha']

    existentes = Usuario.query.filter_by(email=email).all()
    if len(existentes) > 0:
        return jsonify({"message": "E-mail já cadastrado"}), 401
    
    u = Usuario(nome=nome, email=email, senha=senha)

    db.session.add(u)
    db.session.commit()

    return jsonify({"message": "Usuário registrado com sucesso"}), 200



@auth.route("/me", methods=['POST'])
@token_auth.login_required
def me():
    token = request.headers.get("Authorization").replace("Bearer ", "").encode("UTF-8")
    user_id = Serializer.verify_auth_token("froxilda", token)
    user = Usuario.query.get(user_id)
    return jsonify(user.to_dict())