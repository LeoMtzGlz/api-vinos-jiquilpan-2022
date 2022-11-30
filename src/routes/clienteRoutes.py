from flask import Blueprint
from src.extensiones import db
from src.models import Clientes

# Definir el Blueprint para Clientes
cliente = Blueprint('cliente', __name__)

# Definir la ruta CLIENTES
@cliente.route('/api/clientes', methods=['GET','POST'])
def consultar_clientes():
    # Consultar los Clientes
    # SELECT * FROM clientes
    clientes = db.session.query(Clientes).all()
    print(clientes)
    return { 'mensaje': 'Consultado de Clientes exitosa . . . '}


# Definir la ruta CLIENTES
@cliente.route('/api/nuevocliente', methods=['POST'])
def insertar_cliente():
   pass