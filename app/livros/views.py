from flask import request, jsonify, g
from app import db
from app.livros import livros
from app.models import Livro, Usuario
from app.decorators import token_auth, campos_obrigatorios

@livros.route("/todos")
@token_auth.login_required
def pega_livros():
    u = Usuario.query.get(g.current_user)
    lista = u.livros
    retorno = []
    for livro in lista:
        retorno.append(livro.to_dict())
    
    print("teste")

    return jsonify(retorno)

@livros.route("/livro/<int:id>")
@token_auth.login_required
def pega_livro(id):
    livro = Livro.query.get(id)
    if livro:
        if livro.usuario_id == g.current_user:
            return jsonify(livro.to_dict())
        return jsonify({"message": "Este livro não está acessível"})
    return jsonify({"message": "Este livro não existe"})

@livros.route("/livro", methods=['POST'])
@token_auth.login_required
@campos_obrigatorios(["nome","autor"])
def adiciona_livro():
    dados = request.get_json()

    livro = Livro()
    livro.nome = dados['nome']
    livro.autor = dados['autor']

    if "editora" in dados.keys():
        livro.editora = dados['editora']
    
    if "data_lancamento" in dados.keys():
        livro.data_lancamento = dados['data_lancamento']

    livro.usuario_id = g.current_user

    try:
        db.session.add(livro)
        db.session.commit()

        return jsonify({"message": f"Livro {livro.nome} adicionado com sucesso"}), 200
    except Exception as e:
        print(e)
        return jsonify({"message": f"O livro {livro.nome} não pôde ser adicionado"}), 500


@livros.route("/livro/<int:id>", methods=['PUT'])
@token_auth.login_required
def atualiza_livro(id):
    dados = request.get_json()
    livro = Livro.query.get(id)
    if livro:
        if livro.usuario_id == g.current_user:
            if 'nome' in dados.keys():
                livro.nome = dados['nome']
            if 'autor' in dados.keys():
                livro.autor = dados['autor']
            if 'editora' in dados.keys():
                livro.editora = dados['editora']
            if 'data_lancamento' in dados.keys():
                livro.data_lancamento = dados['data_lancamento']
            try:
                db.session.add(livro)
                db.session.commit()

                return jsonify({"message": f"Livro {livro.nome} atualizado com sucesso"}), 200
            except Exception as e:
                print(e)
                return jsonify({"message": f"O livro {livro.nome} não pôde ser atualizado"}), 500
        return jsonify({"message": "Este livro não está acessível"})
    return jsonify({"message": "Este livro não existe"})
            


@livros.route("/livro/<int:id>", methods=['DELETE'])
@token_auth.login_required
def deleta_livro(id):
    livro = Livro.query.get(id)
    if livro:
        if livro.usuario_id == g.current_user:
            Livro.query.filter_by(id=id).delete()
            db.session.commit()
            return jsonify({"message": "Livro apagado com sucesso"})
        return jsonify({"message": "Este livro não está acessível"})
    return jsonify({"message": "Este livro não existe"})
