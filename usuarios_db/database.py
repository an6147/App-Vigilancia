""" Conexión con la base de datos, en este caso con MySQL """
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
""" Conexion """
conexion = 'mysql+pymysql://root:@localhost:3306/app_vigilancia'
""" Uso de SQLAlchemy """
Base = declarative_base()
Session = sessionmaker()
engine = create_engine(conexion, echo=True)


    