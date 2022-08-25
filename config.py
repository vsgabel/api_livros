import os

class Config:
    SSL_REDIRECT = False
    SQLALCHEMY_DATABASE_URI="mysql://aula:123456@localhost:3306/livraria"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY="froxilda"

    @classmethod
    def init_app(cls, app):
        pass

class Heroku(Config):
    SSL_REDIRECT = True if os.getenv("DYNO") else False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://")

    @classmethod
    def init_app(cls, app):
        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

config = {
    'heroku': Heroku,

    'default': Config
}