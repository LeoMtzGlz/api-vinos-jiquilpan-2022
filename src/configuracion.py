class BaseConfig:
    # Variables de configuración base
    DEBUG = True
    SECRET_KEY = "Palabra_Secreta"
    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/vinos_jiquilpan"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True

class DevConfig(BaseConfig):
    # Variables de la clase Padre
    pass

class ProdConfig(BaseConfig):
    DEBUG = False
    TESTING = False