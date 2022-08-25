from sys import prefix
from config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_name])
    db.init_app(app)
    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    from app.auth import auth as auth_bp
    from app.livros import livros as livros_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(livros_bp, url_prefix="/api/biblioteca")

    return app