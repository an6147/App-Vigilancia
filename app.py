# Importación de las librerias principales
from starlette.responses import RedirectResponse, Response, PlainTextResponse, StreamingResponse
from starlette.templating import Jinja2Templates
from vidgear.gears.asyncio import WebGear_RTC
from starlette.requests import Request
from starlette.routing import Route
from pathlib import Path
import uvicorn, cv2
import imutils
import math
import os
#Modulos del Sistema
from modulos import ModC
#Funciones de la Base de Datos "usuarios"
from usuarios_db.db import get_all_usuarios, inicio_session, crear_usuario, get_usuario_by_id, update_usuario, delete_usuario
#Funciones para las Sesiones
from starsessions import CookieStore, SessionAutoloadMiddleware, SessionMiddleware
from starsessions.session import regenerate_session_id
from starlette.middleware import Middleware
#Variable que guardará el directorio de los archivos html
template = Jinja2Templates(directory=os.getcwd()+"\\.vidgear\\webgear_rtc\\templates")
VIDEO_PATH = os.getcwd()+'\\.vidgear\\webgear_rtc\\static\\video\\'
#Clase que recibirá las fuentes de video para procesarlas 
class Custom_Stream_Class:
    #Función para inicializar las fuentes de video
    def __init__(self, source1=None, source2=None, source3=None, source4=None):

        self.source1 = cv2.VideoCapture(source1)
        self.source2 = cv2.VideoCapture(source2)
        self.source3 = cv2.VideoCapture(source3)
        self.source4 = cv2.VideoCapture(source4)

        self.running = True
    #Función para leer los frames de cada una de las fuentes
    def read(self):
        if self.source1 is None or self.source2 is None or self.source3 is None or self.source4 is None:
            return None
        
        if self.running:
            (grabbed1, frame1) = self.source1.read()
            (grabbed2, frame2) = self.source2.read()
            (grabbed3, frame3) = self.source3.read()
            (grabbed4, frame4) = self.source4.read()
            #Si el frame recibido está vacio o no en grabbed*
            if grabbed1 or grabbed2 or grabbed3 or grabbed4:
                """ Como se trata de un solo video con varias fuentes, se utiliza la concatenación
                de frames, en este caso de 4 frames, es decir de 4 cámaras.Al ser una concatenación 
                de mas de 1 fuente, siempre tiene que tener las mismas resoluciones, por eso se 
                redimensionan """ 
                imageOut1 = cv2.resize(frame1,(1341,720), interpolation=cv2.INTER_NEAREST)
                imageOut2 = cv2.resize(frame2,(1341,720), interpolation=cv2.INTER_NEAREST)
                imageOut3 = cv2.resize(frame3,(1341,720), interpolation=cv2.INTER_NEAREST)
                imageOut4 = cv2.resize(frame4,(1341,720), interpolation=cv2.INTER_NEAREST)
                """Una vez las fuentes estén redimensionadas de manera equitativa,
                Se crean 4 condicionales para verificar si en la ruta 'path' está
                vacia o no, si está vacia prosigue con el resto del código, sino,
                se activar el icono de grabando ya que se captó movimiento en la cámara
                correspondiente a ese path """
                path1 = 'c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\Temp\\Cam1'
                dir1 = os.listdir(path1) 
                if (len(dir1) != 0):
                    #Camara 1
                    img1 = imageOut1
                    #REC
                    img2 = cv2.imread('.vidgear/webgear_rtc/static/img/REC2 grisA.png')

                    rows,cols,channels = img2.shape
                    roi = img1[0:rows, 0:cols ]
                    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
                    ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
                    mask_inv = cv2.bitwise_not(mask)
                    img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
                    img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
                    dst = cv2.add(img1_bg,img2_fg)
                    img1[0:rows, 0:cols ] = dst
                    img1[0:rows, 0:cols ] = dst

                    imageOut1 = img1
                #Ruta de la Cámara 2
                path2 = 'c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\Temp\\Cam2'
                dir2 = os.listdir(path2) 
                if (len(dir2) != 0):
                    #Camara 2
                    img1 = imageOut2
                    #REC
                    img2 = cv2.imread('.vidgear/webgear_rtc/static/img/REC2 grisA.png')

                    rows,cols,channels = img2.shape
                    roi = img1[0:rows, 0:cols ]
                    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
                    ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
                    mask_inv = cv2.bitwise_not(mask)
                    img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
                    img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
                    dst = cv2.add(img1_bg,img2_fg)
                    img1[0:rows, 0:cols ] = dst
                    img1[0:rows, 0:cols ] = dst

                    imageOut2 = img1
                #Ruta de la Cámara 3
                path3 = 'c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\Temp\\Cam3'
                dir3 = os.listdir(path3) 
                if (len(dir3) != 0):
                    #Camara 3
                    img1 = imageOut3
                    #REC
                    img2 = cv2.imread('.vidgear/webgear_rtc/static/img/REC2 grisA.png')

                    rows,cols,channels = img2.shape
                    roi = img1[0:rows, 0:cols ]
                    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
                    ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
                    mask_inv = cv2.bitwise_not(mask)
                    img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
                    img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
                    dst = cv2.add(img1_bg,img2_fg)
                    img1[0:rows, 0:cols ] = dst
                    img1[0:rows, 0:cols ] = dst

                    imageOut3 = img1
                #Ruta de la Cámara 4
                path4 = 'c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\Temp\\Cam4'
                dir4 = os.listdir(path4) 
                if (len(dir4) != 0):
                    #Camara 4
                    img1 = imageOut4
                    #REC
                    img2 = cv2.imread('.vidgear/webgear_rtc/static/img/REC2 grisA.png')

                    rows,cols,channels = img2.shape
                    roi = img1[0:rows, 0:cols ]
                    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
                    ret, mask = cv2.threshold(img2gray, 200, 255, cv2.THRESH_BINARY)
                    mask_inv = cv2.bitwise_not(mask)
                    img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
                    img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
                    dst = cv2.add(img1_bg,img2_fg)
                    img1[0:rows, 0:cols ] = dst
                    img1[0:rows, 0:cols ] = dst

                    imageOut4 = img1
                """Se redimensionan los 4 frames de manera tal que tengan la misma altura """
                frame1 = imutils.resize(imageOut1, height = (imageOut1.shape[0] // 2))
                frame2 = imutils.resize(imageOut2, height = (imageOut2.shape[0] // 2))
                frame3 = imutils.resize(imageOut3, height = (imageOut3.shape[0] // 2))
                frame4 = imutils.resize(imageOut4, height = (imageOut4.shape[0] // 2))
                """Se concatenan primero de manera vertical, el frame1 con el frame 2 en un sólo frame
                Y luego frame3 con el frame 4 en un solo frame"""
                concat_v = cv2.vconcat([frame1, frame2])
                concat_v2 = cv2.vconcat([frame3, frame4])
                """Se concatenan los 2 nuevos frames de manera horizontal en uno solo"""
                concat_h = cv2.hconcat([concat_v, concat_v2])
                """Se retorna el nuevo frame el cual es el que se visualizará en la web"""
                return concat_h
            else:
                self.running = False
        return None
    #Función para detener las fuentes cuando ya no estén en uso
    def stop(self):
        self.running = False

        if not self.source1 is None:
            self.source1.release()
        if not self.source2 is None:
            self.source2.release()
        if not self.source3 is None:
            self.source3.release()
        if not self.source3 is None:
            self.source3.release()
        if not self.source4 is None:
            self.source4.release()
#FUNCIONES DE RETORNO
"""Función para mostrar la página asociada al Login"""
async def login(request: Request)->Response:
    """Entrará en esta condicional si desde el formulario se envian datos para iniciar la sesion"""
    if request.method == "POST":
        """Variable que recibirá los datos del formulario"""
        usuario_data = await request.form()
        """Variable que guardará al usuario en caso de que exista en la base de datos"""
        logged_user = inicio_session(usuario_data['username'], usuario_data['password'])
        """Comprobando si la variable está vacia o de si tiene guardada algún usuario"""
        if logged_user != None:
            """Si tiene algún usuario se procede a verificar si la contraseña es correcta o no"""
            if logged_user.password ==  usuario_data['password']:
                """Si lo es, se guarda el nombre completo y el tipo de acceso"""
                request.session['fullname'] = logged_user.fullname
                request.session['tipo_de_acceso'] = logged_user.tipo_de_acceso
                """Se crea un sesión asociada al usuario que ha ingresado"""
                regenerate_session_id(request)
                """ Se comprueba del tipo de acceso que tiene el usuario ingresado"""
                if(logged_user.tipo_de_acceso=="Administrador"):
                    """Si es de tipo Administrador es redirigido a la página principal con la opción de Usuarios 
                    habilitada para poder editar a los usuarios registrados o crear nuevos"""
                    return RedirectResponse(request.url_for('camaras'), status_code=303)
                else:
                    """Si es de tipo Usuario es redirigido a la página principal pero con la opción de Usuarios 
                    deshabilitada"""
                    return RedirectResponse(request.url_for('camaras'), status_code=303)
            else:
                """Si la contraseña no es correcta, se renderizará la página del Login mostrando un mensaje
                de error con respecto a la contraseña"""
                error = "Contraseña Incorrecta"
                nombre = usuario_data['username']
                cont = usuario_data['password']
                context = {"request": request, "error":error, "nombre":nombre, "cont":cont}
                return template.TemplateResponse("login.html",context)
        else:
            """Si no existe un usuario ingresado con los datos proporcionados en el formulario, se renderizará 
            la página del Login mostrando un mensaje de error con respecto al usuario"""
            error = "Usuario No Encontrado"
            nombre = usuario_data['username']
            cont = usuario_data['password']
            context = {"request": request, "error":error, "nombre":nombre, "cont":cont}
            return template.TemplateResponse("login.html",context)
    else:
        """Se renderizará la pagina del login al ingresar a la aplicación por primera vez"""
        error = ''
        nombre = ''
        cont =   ''   
        context = {"request": request, "error":error, "nombre":nombre, "cont":cont}
        return template.TemplateResponse("login.html",context)
"""Función para cerrar la sesión del sistema"""    
async def logout(request: Request)->Response:
    """De esta manera se cierra y se limpia la sesión actual"""
    request.session.clear()
    """Después de haber cerrado la sesión, se redirige a la página del login"""
    return RedirectResponse(request.url_for('login'), status_code=303)
"""Función para mostrar el dashboard"""
async def dashboard(request: Request)->Response:
    """Se guarda el nombre completo y el tipo de acceso del usuario que ha iniciado sesion"""
    name = request.session.get("fullname")
    acceso = request.session.get("tipo_de_acceso")
    """Entrará en esta condicional si desde el formulario se envian datos para registrar a un nuevo usuario"""
    if request.method == "POST":
        """Variable que recibirá los datos del formulario"""
        usuario_data = await request.form()
        """Se guardan los datos obtenidos de manera individual"""
        usuario = usuario_data['username']
        contrasena = usuario_data['password']
        confirmar = usuario_data['confirm_password']
        nombreCompleto= usuario_data['fullname']
        tipo = usuario_data['tipo_de_acceso']
        """Se pasan como parámetros a una variable para crear una tupla"""
        datos = {'username': usuario, 'password': contrasena, 'confirm_password': confirmar,'fullname': nombreCompleto, 'tipo_de_acceso': tipo}
        """Se envia la tupla de datos a la función que creará y agregará al nuevo usuario a la base de datos"""
        crear_usuario(datos)
        """Se redirige a la pagina asociada con el dashboard"""
        return RedirectResponse(request.url_for('dashboard'), status_code=303)
    """Cuando se carga por primera vez la página, se obtienen todos los usuarios existentes en la base de datos"""
    usuarios = get_all_usuarios()
    """Se envian los datos que la página utilizará"""    
    context = {"request": request, "usuarios": usuarios, "name": name, "tipo": acceso}
    """Se renderiza la página del dashboard"""
    return template.TemplateResponse("dashboard.html",context)
"""Función para actualizar un usuario"""
async def update(request:Request)->Response:
    """Variables para recuperar la información del usuario al que se le actualizarán los datos"""
    usuario_id = request.path_params.get('usuario_id')
    name = request.session.get("fullname")
    acceso = request.session.get("tipo_de_acceso")
    """Se recupera el id asociado al usuario a actualizar"""
    usuarioUpdate = get_usuario_by_id(usuario_id)
    """Entrará en esta condicional si desde el formulario se envian datos para actualizar"""
    if request.method == "POST":
        """Variable que recibirá los datos del formulario"""
        usuario_update_data = await request.form()
        """Se guardan los datos obtenidos de manera individual"""
        usuario = usuario_update_data['username']
        contrasena = usuario_update_data['password']
        confirmar = usuario_update_data['confirm_password']
        nombreCompleto= usuario_update_data['fullname']
        tipo = usuario_update_data['tipo_de_acceso']
        """Se pasan como parámetros a una variable para crear una tupla"""
        datos = {'username': usuario, 'password': contrasena, 'confirm_password': confirmar,'fullname': nombreCompleto, 'tipo_de_acceso': tipo}
        """Se envia la tupla de datos a la función que actualizará al usuario en la base de datos"""
        update_usuario(usuario_id, datos)
        """Se redirige a la pagina asociada con el dashboard"""
        return RedirectResponse(request.url_for('dashboard'), status_code=303)
    """Se envian los datos que la página utilizará"""
    context = {"request": request, "usuario": usuarioUpdate, "name": name, "tipo": acceso}
    """Se renderizará la página para editar al usuario"""
    return template.TemplateResponse("editarUsuario.html",context)
"""Función para eliminar un usuario"""
async def delete(request:Request):
    """Se recupera el id asociado al usuario a eliminar"""
    usuario_id = request.path_params.get('usuario_id')
    """Función para eliminar al usuario de la base datos"""
    delete_usuario(usuario_id)
    """Una vez eliminado, se redirige a la página del dashboard"""
    return RedirectResponse(request.url_for('dashboard'), status_code=303) 
"""Función para renderizar la pagína que muestran las fuentes de video (Camaras)"""
async def camaras(request:Request)->Response:
    """Variables para recuperar información del usuario que inició sesión"""
    name = request.session.get("fullname")
    tipo = request.session.get("tipo_de_acceso")
    """Se envian los datos que la página utilizará"""
    context = {"request": request, "name": name, "tipo": tipo}
    """ Se renderiza página asociada a las cámaras """
    return template.TemplateResponse("index.html", context)
""" Funcion para el video Ondemand"""
async def video_streaming(request: Request) -> StreamingResponse:
    path = Path(VIDEO_PATH + request.query_params['video'])
    print(request.query_params['video'])
    file = path.open('rb')
    file_size = path.stat().st_size

    content_range = request.headers.get('range')

    content_length = file_size
    status_code = 200
    headers = {}

    if content_range is not None:
        content_range = content_range.strip().lower()

        content_ranges = content_range.split('=')[-1]

        range_start, range_end, *_ = map(str.strip, (content_ranges + '-').split('-'))

        range_start = max(0, int(range_start)) if range_start else 0
        range_end   = min(file_size - 1, int(range_end)) if range_end else file_size - 1

        content_length = (range_end - range_start) + 1

        file = ModC.ranged(file, start = range_start, end = range_end + 1)

        status_code = 206

        headers['Content-Range'] = f'bytes {range_start}-{range_end}/{file_size}'

    response = StreamingResponse \
    (
        file,
        media_type = 'video/mp4',
        status_code = status_code,
    )

    response.headers.update \
    ({
        'Accept-Ranges': 'bytes',
        'Content-Length': str(content_length),
        **headers,
    })

    return response
"""Función para renderizar la pagína que muestra el buscador de videos"""
async def ondemand(request:Request)->Response:
    """Variables para recuperar información del usuario que inició sesión"""
    name = request.session.get("fullname")
    tipo = request.session.get("tipo_de_acceso")
    nombre_video = 'Bola dragon.mp4'
    context = {"request": request, "name": name, "tipo": tipo, "nombre_video": nombre_video}
    """Se renderiza página asociada al buscador de videos"""
    return template.TemplateResponse("ondemand.html", context)
"""Función para renderizar la pagína asociada a la busqueda"""
async def busqueda(request: Request)->Response:
    """Variables para recuperar información del usuario que inició sesión"""
    name = request.session.get("fullname")
    tipo = request.session.get("tipo_de_acceso")
    """Variables para guardar la paginación"""
    videos_x_pagina = 20
    total_videos = 81
    total_paginas = int(math.ceil(total_videos/videos_x_pagina))
    total_paginas_b = int(total_videos/videos_x_pagina)
    nombre_video = 'Bola dragon.mp4'
    """Se envian los datos que la página utilizará"""
    context = {"request": request, "total_paginas": total_paginas, "videos_x_pagina": videos_x_pagina, "total_videos": total_videos, "total_paginas_b": total_paginas_b, "name": name, "tipo": tipo, "nombre_video": nombre_video}
    """ Se renderiza página asociada a la busqueda """
    return template.TemplateResponse("busqueda.html", context)
""" Funcion de consulta para traer los datos del formulario con respecto a las fechas """
async def consulta(request: Request)->Response:
    form = await request.form()
    print(form['dateStart'])
    print(form['dateEnd'])
    return PlainTextResponse('Hola Mundo' + form['fecha_inicial'] + ' ' + form['fecha_final'] + ' ' + form['criterio_fecha'] + ' fecha Inicial' + form['dateStart'] + ' fecha final' + form['dateEnd'] + form['mes'])
"""Configuración que recibe el WebGear_RTC con respecto a la fuentes de video """
options = {"custom_data_location": "./", #Opción para guardar el proyecto en la dirección actual
            "enable_infinite_frames": True, #Se mostrarán frames en caso de que la conexion con las cámaras se cierre 
            #"enable_live_broadcast": True, #Habilitar conexión para multiples clientes
            #"custom_stream": Custom_Stream_Class(source1=1, source2=1, source3=1, source4= 1)} #Establecer videos como fuentes y no cámaras
           "custom_stream": Custom_Stream_Class(source1 = os.getcwd()+"\\.vidgear\\webgear_rtc\\static\\video\\v1.mp4", source2 = os.getcwd()+"\\.vidgear\\webgear_rtc\\static\\video\\v2.mp4", source3 = os.getcwd()+"\\.vidgear\\webgear_rtc\\static\\video\\v3.mp4" , source4 = os.getcwd()+"\\.vidgear\\webgear_rtc\\static\\video\\v4.mp4")}
            #Establecer las cámaras como fuentes de video
#Creando la instancia WEbGear_RTC con sus parámetros            
web = WebGear_RTC(logging=True, stabilize=True, time_delay=0, **options)
#Estableciendo parámetros para el manejo de las sesiones
web.middleware =[
    Middleware(SessionMiddleware, store=CookieStore(secret_key="v8$I9p50l$%Z"), cookie_https_only=False),
    Middleware(SessionAutoloadMiddleware),
]
"""RUTAS para las páginas"""
web.routes.append(Route("/camaras", endpoint=camaras, methods=["GET", "POST"]))
web.routes.append(Route("/ondemand", endpoint=ondemand, methods=["GET", "POST"]))
web.routes.append(Route("/ondemand/busqueda", endpoint=busqueda, methods=["GET", "POST"]))
web.routes.append(Route("/video_streaming", endpoint=video_streaming, methods=["GET", "POST"]))
web.routes.append(Route("/consulta", endpoint=consulta, methods=["GET", "POST"]))
web.routes.append(Route("/login", endpoint=login, methods=["GET", "POST"]))
web.routes.append(Route("/dashboard", endpoint=dashboard, methods=["GET", "POST"]))
web.routes.append(Route("/update/{usuario_id:int}/", endpoint=update, methods=["GET", "POST"]))
web.routes.append(Route("/delete/{usuario_id:int}/", endpoint=delete))
web.routes.append(Route("/logout", endpoint=logout))
"""Levantamiento del servidor"""
uvicorn.run(web(), host="0.0.0.0", port=8000)
"""Función para cerrar el servidor"""
web.shutdown()