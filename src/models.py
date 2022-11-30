from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .extensiones import db

class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clienteNombre  = db.Column(db.String(100), nullable=False)
    clienteApellidos = db.Column(db.String(100), nullable=False)
    clienteRFC = db.Column(db.String(15))
    clienteEmail = db.Column(db.String(100), unique=True, nullable=False)
    clientePassword = db.Column(db.String(300), nullable=False)
    confirmado = db.Column(db.Boolean, default=False )  # Valor por default


class Categoria(db.Model): # Nombre de la Clase
    __tablename__ = 'categorias' # Aqui se define el nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombreCategoria = db.Column(db.String(100), nullable=True)
    descripcionCategoria = db.Column(db.String(400))
    banderaDescuento = db.Column(db.Integer, default=False)
    descuentoCategoria = db.Column(db.Integer, default=0)
    imagenCategoria = db.Column(db.String(50), default='imagenDefault.jpg')
    
    productos = db.relationship('Producto', backref='categorias')

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