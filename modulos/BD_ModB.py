import pymysql
    
def obtener_conexion(host_name, user_name, user_pass, db_name):
    return pymysql.connect( host=host_name,
                            user=user_name,
                            password=user_pass,
                            db=db_name)


def insertar_video(nombre, fecha, ruta_video, ruta_miniatura, comentario):

    try:
        conexion = obtener_conexion('localhost', 'root', '', 'eventos')
        try:
            with conexion.cursor() as cursor:
                consulta = "INSERT INTO video(NOMBRE, FECHA, RUTA_VIDEO, RUTA_MINIATURA, COMENTARIO) VALUES (%s, %s, %s, %s, %s);"
                #Podemos llamar a .execute con datos distintos
                cursor.execute(consulta, (nombre, fecha, ruta_video, ruta_miniatura, comentario))
            conexion.commit()
        finally:
            conexion.close()
            return True
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        return False


def lectura_all():
    try:
        conexion = obtener_conexion('localhost', 'root', '', 'eventos')
        try:
            with conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT * FROM video;")
                # El caracter * se refiere o selecciona a todos los campos de la tabla video
                # Con fetchall traemos todas las filas
                all = cursor.fetchall()
        finally:
            conexion.close()
            return all
        
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        return False


def lectura_intervalo_fechas(fecha_inicial, fecha_final):

    try:
        conexion = obtener_conexion('localhost', 'root', '', 'eventos')
        try:
            with conexion.cursor() as cursor:  
                consulta = "SELECT * FROM video WHERE FECHA BETWEEN %s and %s;"
                cursor.execute(consulta, (fecha_inicial, fecha_final))
                # Con fetchall traemos todas las filas
                resultado = cursor.fetchall()
        finally:
            conexion.close()
            return resultado
        
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        return False


def lectura_ID(id):

    try:
        conexion = obtener_conexion('localhost', 'root', '', 'eventos')
        try:
            with conexion.cursor() as cursor:             
                consulta = "SELECT * FROM video WHERE ID = %s;"
                cursor.execute(consulta, (id))
                # Con fetchall traemos todas las filas que coincidan
                resultado = cursor.fetchall()
        finally:
            conexion.close()
            return resultado
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        return False


def eliminar_intervalo_fechas(fecha_inicial, fecha_final):

    try:
        conexion = obtener_conexion('localhost', 'root', '', 'eventos')
        try:
            with conexion.cursor() as cursor:
                
                numero_de_registros = "SELECT COUNT(*) FROM video WHERE FECHA BETWEEN %s and %s;"
                cursor.execute(numero_de_registros, (fecha_inicial, fecha_final))
                resultado = cursor.fetchone()
                # Retornar solo un registro (numero de registros a eliminados)

                consulta = "DELETE FROM video WHERE FECHA BETWEEN %s and %s;"
                cursor.execute(consulta, (fecha_inicial, fecha_final))
            # No olvidemos hacer commit cuando hacemos un cambio a la BD
            conexion.commit()
        finally:
            conexion.close()
            return resultado
        
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        return False


def eliminar_ID(id):
    try:
        conexion = obtener_conexion('localhost', 'root', '', 'eventos')
        try:
            with conexion.cursor() as cursor:
                
                consulta = "DELETE FROM video WHERE ID = %s;"
                cursor.execute(consulta, (id))
    
            # No olvidemos hacer commit cuando hacemos un cambio a la BD
            conexion.commit()
        finally:
            conexion.close()
            return True
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        return False

