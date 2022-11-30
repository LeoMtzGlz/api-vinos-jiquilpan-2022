from flask import Blueprint
from src.extensiones import db
from src.models import Producto

# Definir el Blueprint para Clientes
producto = Blueprint('producto', __name__)

# Definir la ruta PRODUCTOS
@producto.route('/api/productos', methods=['GET'])
def consultar_productos():
    # Consultar los Productos
    # SELECT * FROM productos
    lista_productos = db.session.query(Producto).all()
    print(lista_productos)
    for p in lista_productos:
        print(p)
    return { 'mensaje': 'Consultado Productos . . . '}