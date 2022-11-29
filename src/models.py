
from .extensiones import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clienteNombre  = db.Column(db.String(100), nullable=False)
    clienteApellidos = db.Column(db.String(100), nullable=False)
    clienteRFC = db.Column(db.String(15))
    clienteEmail = db.Column(db.String(100), unique=True, nullable=False)
    clientePassword = db.Column(db.String(300), nullable=False)
    confirmado = db.Column(db.Boolean, default=False )  # Valor por default