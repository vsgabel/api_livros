from flask import Blueprint

livros = Blueprint('livros', __name__)

from app.livros.views import *