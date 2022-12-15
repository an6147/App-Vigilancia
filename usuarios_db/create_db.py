""" Creación de la Base de datos con respecto a la Base y al Engine"""
from .database import Base, engine
from .models import Usuario

Base.metadata.create_all(bind=engine)