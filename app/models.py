from app import db
from app.serializer import Serializer
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)
    livros = db.relationship('Livro', backref="usuario")

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email
        }

    @property
    def senha(self):
        raise AttributeError("Operação não permitida")

    @senha.setter
    def senha(self, valor):
        self.senha_hash = generate_password_hash(valor)

    def verifica_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    @staticmethod
    def verifica_token(token):
        return Serializer.confirm("froxilda", token)

class Livro(db.Model):
    __tablename__ = "livro"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), nullable=False)
    autor = db.Column(db.String(64), nullable=False)
    editora = db.Column(db.String(64))
    data_lancamento = db.Column(db.Date)
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "autor": self.autor,
            "editora": self.editora,
            "data_lancamento": self.data_lancamento
        }