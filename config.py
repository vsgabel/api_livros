class Config:
    SQLALCHEMY_DATABASE_URI="mysql://aula:123456@localhost:3306/livraria"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY="froxilda"

config = {
    'default': Config
}