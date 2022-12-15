""" Modelo de la tabla 'usuario' existente en la base de datos 'app_vigilancia' """
from .database import Base
from sqlalchemy import Column, String, Integer, VARCHAR, CHAR
""" Clase Usuario, modelo de la tabla usuario """
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer(), primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(CHAR(120),nullable=False, unique=True)
    confirm_password = Column(CHAR(120),nullable=False, unique=True)
    fullname = Column(VARCHAR(50), nullable=False, unique=False)
    tipo_de_acceso = Column(VARCHAR(20), nullable=False, unique=False)

    def __repr__(self):
        return f"<Usuario {self.username}>"