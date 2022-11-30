from flask import Blueprint
from src.extensiones import db
from src.models import Categoria

# Definir el Blueprint para Clientes
categoria = Blueprint('categoria', __name__)

# Definir la ruta CATEGORIAS
@categoria.route('/api/categorias', methods=['GET'])
def consultar_categorias():
    # Consultar los Categorias
    # SELECT * FROM categorias
    categorias = db.session.query(Categoria).all()
    print(categorias)
    return { 'mensaje': 'Consultado de Categorias . . . '}