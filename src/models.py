import bcrypt
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, exc
import datetime
import jwt
from .extensiones import db

class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clienteNombre  = db.Column(db.String(100), nullable=False)
    clienteApellidos = db.Column(db.String(100), nullable=False)
    clienteRFC = db.Column(db.String(15))
    clienteEmail = db.Column(db.String(100), unique=True, nullable=False)
    clientePassword = db.Column(db.String(300), nullable=False)
    confirmado = db.Column(db.Boolean, default=False )  # Valor por default

    pedidos = db.relationship('Pedido', backref='clientes')  #

    def registrar_cliente(self, datos):
        # Crear una respuesta
        msg ="Cliente insertado correctamente"
        respuesta = {'estatus': "OK-1", "codigo":"", "mensaje": msg }

        self.clienteNombre = datos['nombre']
        self.clienteEmail = datos['correo']
        self.clientePassword = self.cifrar_contrasena( datos['clave'] )
        try:
            db.session.add(self)
            db.session.commit()
            respuesta["codigo"] = '1' # Todo es correcto
        except exc.SQLAlchemyError as error:
            print(error)
            campo = error.__cause__.args[1].split("'")[3]
            valor = error.__cause__.args[1].split("'")[1]
            respuesta["codigo"] = error.__cause__.args[0]
            respuesta["mensaje"] = "Ocurrió un error para el campo: " + campo
            respuesta["mensaje"] = respuesta["mensaje"] + " en la entrada de datos: " + valor
        return respuesta

    def cifrar_contrasena(self, contrasena):
        salt = bcrypt.gensalt()
        contrasena_cifrada = bcrypt.hashpw(contrasena.encode('utf-8'),salt)
        return contrasena_cifrada

    def verificar_contrasena(self, clave, clave_cifrada):
        return bcrypt.checkpw(clave.encode('utf-8'), clave_cifrada.encode('utf-8'))
    def validar_cliente(self,correo, clave):
        # 1 Crear una respuesta
        msg = "Cliente encontrado"
        respuesta = {'estatus': "OK-1",
                     "codigo": "",
                     "mensaje": msg,
                     "token": "",
                     "datos" : {}
                     }
        # 2. Crear la consulta
        cli = Clientes.query.filter(Clientes.clienteEmail == correo).first()
        if cli:
            # Verificar la contraseña
            if self.verificar_contrasena(clave, cli.clientePassword):
                msg = " Cliente Autenticado "
                # Generar el token
                respuesta["token"] = self.generar_token(cli)
                respuesta["datos"] = {
                    'id': cli.id,
                    'nombre': cli.clienteNombre,
                    'ap': cli.clienteApellidos,
                    'correo': cli.clienteEmail
                }
            else:
                msg = " Cliente No Autenticado "
            respuesta["mensaje"]: msg
        else:
            msg = "No encontrado"
        respuesta["mensaje"] = msg
        return respuesta

    def generar_token(self, cliente):
        secreto = "Palabra_Secreta"
        token = jwt.encode({
            'id': cliente.id,
            'nombre': cliente.clienteNombre,
            'ap': cliente.clienteApellidos,
            'correo': cliente.clienteEmail
        },
        secreto,
        algorithm = 'HS256'
        )
        return token



class Categoria(db.Model): # Nombre de la Clase
    __tablename__ = 'categorias' # Aqui se define el nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombreCategoria = db.Column(db.String(100), nullable=True)
    descripcionCategoria = db.Column(db.String(400))
    banderaDescuento = db.Column(db.Integer, default=False)
    descuentoCategoria = db.Column(db.Integer, default=0)
    imagenCategoria = db.Column(db.String(50), default='imagenDefault.jpg')
    
    productos = db.relationship('Producto', backref='categorias') #

class Producto(db.Model):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    idCategoria = Column(Integer, ForeignKey('categorias.id'))
    productoNombreCorto = Column(String(100), unique=True, nullable=False)
    productoNombreLargo = Column(String(200))
    productoDescripcion = Column(String(200))
    productoTipo = Column(Integer, default=1)
    productoPresentacion = Column(String(20), default='Botella')
    productoCosto = Column(Integer, nullable=False)
    productoGanancia = Column(Integer, nullable=False, default=20)
    productoDescuento = Column(Integer, default=0)
    productoExistencia = Column(Integer, default=1000)
    productoImagen = Column(String(50), default= 'imagenDefault.jpg')


# Relación muchoas a Muchos
detalle_pedidos = db.Table('detallepedidos',
    db.Column('id', db.Integer, primary_key = True),
    db.Column('idProducto', db.Integer, db.ForeignKey('productos.id')),
    db.Column('idPedido', db.Integer, db.ForeignKey('pedidos.id')),
    db.Column('cantidad', db.Integer,  nullable = False),
    db.Column('utilidad', db.Integer),
    db.Column('descuento', db.Integer, default = 0),
    db.Column('precioFinal', db.Integer, nullable = False ),
    db.Column('subTotal', db.Integer, nullable = False)
    )

class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key = True)
    idCliente = Column(Integer, ForeignKey('clientes.id'))
    fecha = Column(Date, default = datetime.datetime)
    total = Column(Integer, default = 0.0)
    iva = Column(Integer, nullable=False)
    descuento = Column(Integer, default = 0.0)
    pagado = Column(Boolean, default = False)
    estado = Column(Integer, default = 1)

    # Establecer la relación Muchoa a Muchos con detallepedidos
    producto_pedidos = db.relationship('Producto',
                                       secondary = detalle_pedidos,
                                       backref = db.backref('pedidos')) # lazy=True

