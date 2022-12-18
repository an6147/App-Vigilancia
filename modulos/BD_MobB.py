import pymysql
import mysql.connector



def main():
    conexion_db()
    #lectura_all()
    #lectura_intervalo_fechas()
    #lectura_ID()
    #eliminar_intervalo_fechas("1900-01-01", "2022-12-12",)
    #eliminar_ID()

    
def conexion_db():
    try:
        conexion = pymysql.connect(host = 'localhost',
                                   user = 'root',
                                   password = '',
                                   db = 'eventos')

        #print("Conexión correcta con el servidor")
        return True
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        #print("Ocurrió un error al conectar con el servidor: ", e)
        return False

def insertar_video(in_nombre, in_fecha, in_direc_video, in_direc_mini, in_comen, in_duracion):
    nombre = in_nombre
    fecha = in_fecha
    direc_video = in_direc_video
    direc_mini = in_direc_mini
    comen = in_comen
    duracion = in_duracion
    try:
        conexion = pymysql.connect( host = 'localhost',
                                    user = 'root',
                                    password = '',
                                    db = 'eventos')
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO registro(NOMBRE, FECHA, DIREC_VIDEO, DIREC_MINI, COMEN, DURACION) VALUES (%s, %s, %s, %s, %s, %s);"
                #Podemos llamar a .execute con datos distintos
                cursor.execute(consulta, (nombre, fecha, direc_video, direc_mini, comen, duracion))
            conexion.commit()
        finally:
            conexion.close()
            return True
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        return False

def lectura_all():
    try:
        conexion = pymysql.connect( host = 'localhost',
                                    user = 'root',
                                    password = '',
                                    db = 'eventos')
        try:
            with conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT ID, NOMBRE, FECHA, DIREC_VIDEO, DIREC_MINI, COMEN, DURACION FROM registro;")
                # Con fetchall traemos todas las filas
                all = cursor.fetchall()
        finally:
            conexion.close()
            return all
        
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        return False

def lectura_intervalo_fechas(in_fecha1, in_fecha2):
    fecha1 = in_fecha1
    fecha2 = in_fecha2
    try:
        conexion = pymysql.connect( host = 'localhost',
                                    user = 'root',
                                    password = '',
                                    db = 'eventos')
        try:
            with conexion.cursor() as cursor:  
                consulta = "SELECT ID, NOMBRE, FECHA, DIREC_VIDEO, DIREC_MINI, COMEN, DURACION FROM registro WHERE FECHA BETWEEN %s and %s;"
                cursor.execute(consulta, (fecha1, fecha2))
                # Con fetchall traemos todas las filas
                resultado = cursor.fetchall()
        finally:
            conexion.close()
            return resultado
        
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        return False

def lectura_ID(in_id):
    id = in_id
    try:
        conexion = pymysql.connect( host = 'localhost',
                                    user = 'root',
                                    password = '',
                                    db = 'eventos')
        try:
            with conexion.cursor() as cursor:             
                consulta = "SELECT ID, NOMBRE, FECHA, DIREC_VIDEO, DIREC_MINI, COMEN, DURACION FROM registro WHERE ID = %s;"
                cursor.execute(consulta, (id))
                # Con fetchall traemos todas las filas que coincidan
                resultado = cursor.fetchall()
        finally:
            conexion.close()
            return resultado
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        return False

def eliminar_intervalo_fechas(in_fecha1, in_fecha2):
    fecha1 = in_fecha1
    fecha2 = in_fecha2
    try:
        conexion = pymysql.connect( host = 'localhost',
                                    user = 'root',
                                    password = '',
                                    db = 'eventos')
        try:
            with conexion.cursor() as cursor:
                
                consulta = "DELETE FROM registro WHERE FECHA BETWEEN %s and %s;"
                cursor.execute(consulta, (fecha1, fecha2))
    
            # No olvidemos hacer commit cuando hacemos un cambio a la BD
            conexion.commit()
        finally:
            conexion.close()
            return True
        
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        return False

def eliminar_ID(in_id):
    ID = in_id
    try:
        conexion = pymysql.connect( host = 'localhost',
                                    user = 'root',
                                    password = '',
                                    db = 'eventos')
        try:
            with conexion.cursor() as cursor:
                
                consulta = "DELETE FROM registro WHERE ID = %s;"
                cursor.execute(consulta, (ID))
    
            # No olvidemos hacer commit cuando hacemos un cambio a la BD
            conexion.commit()
        finally:
            conexion.close()
            return True
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        return False


main()