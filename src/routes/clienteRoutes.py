from flask import Blueprint, request
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
@cliente.route('/api/clientes/registrar', methods=['POST'])
def insertar_cliente():
    # Leer los datos enviados
    # Recibir datos desde un formulario request.form['nombre']
    json_cliente = request.get_json()
    for clave, valor in json_cliente.items():
        print(clave, valor)

    cliente = Clientes()
    return cliente.registrar_cliente(json_cliente)

@cliente.route('/api/clientes/login', methods=['POST'])
def login_cliente():
    json_cliente = request.get_json()
    for clave, valor in json_cliente.items():
        print(clave, valor)

    cliente = Clientes()
    return cliente.validar_cliente( json_cliente['correo'],json_cliente['clave'] )

