
from flask import Flask
from flask_cors import CORS

from .extensiones import db

# from src.categorias.routes import categoria

def create_app():
    app = Flask(__name__)
    # Configurar las referencias cruzadas, cuando se hacen peticiones de otros dominios
    CORS(app)
    # Agregar configuración desde archivo configuracion.txt
    app.config.from_object('configuracion.DevConfig')

    # Configurar SQLAlchemy
    db.init_app(app) #  ***************FALTÓ PASARLE LA APLICACIÓN (app)

    # Registramos los Blueprints

    return app

