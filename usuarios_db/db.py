""" Funciones para manipulación de la Base de datos """
from .database import Session,engine
from .models import Usuario

local_session = Session(bind=engine)
""" Función que retornará a todos los usuarios """
def get_all_usuarios():
    return local_session.query(Usuario).all()
""" Función para crear a un nuevo usuario """
def crear_usuario(usuario_data):
     new_user = Usuario(**usuario_data)

     try:
        local_session.add(new_user)
        local_session.commit()
     except:
        local_session.rollback()
     finally:
        local_session.close()
""" Función para retornar un usuario por su id """
def get_usuario_by_id(usuario_id):
    return local_session.query(Usuario).filter_by(id=usuario_id).first()
""" Función para comprobar si existe el usuario ingresado """
def inicio_session(usuario, contrasena):

    try:
        row = local_session.query(Usuario).filter_by(username=usuario).first()
        if row != None:
            return row  
        else:
            return None
    except:
        local_session.rollback()
    finally:
        local_session.close() 
""" Función para actualizar un usuario """
def update_usuario(usuario_id, usuario_data):
    usuario_a_actualizar = get_usuario_by_id(usuario_id)

    usuario_a_actualizar.username = usuario_data["username"]
    usuario_a_actualizar.password = usuario_data["password"]
    usuario_a_actualizar.confirm_password = usuario_data["confirm_password"]
    usuario_a_actualizar.fullname = usuario_data["fullname"]
    usuario_a_actualizar.tipo_de_acceso = usuario_data["tipo_de_acceso"]

    local_session.commit()
""" Función para eliminar un usuario """
def delete_usuario(usuario_id):
    usuario_a_eliminar = get_usuario_by_id(usuario_id)

    local_session.delete(usuario_a_eliminar)
    local_session.commit()
