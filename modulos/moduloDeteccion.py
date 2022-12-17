import cv2
import numpy as np
from datetime import datetime
import time
import threading
#import BD_MobB
import shutil
import os

def main():
	#Creacion de las carpetas
	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello', exist_ok = True)

	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\Temp', exist_ok = True)
	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\Temp\\Cam1', exist_ok = True)
	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\Temp\\Cam2', exist_ok = True)
	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\Temp\\Cam3', exist_ok = True)
	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\Temp\\Cam4', exist_ok = True)

	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\thumbnail', exist_ok = True)
	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\thumbnail\\Cam1', exist_ok = True)
	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\thumbnail\\Cam2', exist_ok = True)
	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\thumbnail\\Cam3', exist_ok = True)
	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\thumbnail\\Cam4', exist_ok = True)

	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\videos', exist_ok = True)
	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\videos\\Cam1', exist_ok = True)
	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\videos\\Cam2', exist_ok = True)
	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\videos\\Cam3', exist_ok = True)
	os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\videos\\Cam4', exist_ok = True)

	folder_temp_direc = 'c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\Temp\\Cam'
	folder_thumbnail_direc = 'c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\thumbnail\\Cam'
	folder_videos_direc = 'c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\videos\\Cam'

	#Acá se establece las fuentes de video
	index1 = 0
	#index2 = "http://192.168.1.100:4747/video"
	#index3 = 3
	#index4 = 4
	
	#Se definen los hilos de trabajo
	hilo1 = threading.Thread(target = detectar_y_grabar, args = (index1, 1, folder_temp_direc, folder_thumbnail_direc, folder_videos_direc,))
	#hilo2 = threading.Thread(target = detectar_y_grabar, args = (index2, 2, folder_temp_direc, folder_thumbnail_direc, folder_videos_direc,))
	#hilo3 = threading.Thread(target = detectar_y_grabar, args = (index3, 3, folder_temp_direc, folder_thumbnail_direc, folder_videos_direc,))
	#hilo4 = threading.Thread(target = detectar_y_grabar, args = (index4, 4, folder_temp_direc, folder_thumbnail_direc, folder_videos_direc,))

	#Se da inicio a cada hilo
	hilo1.start()
	#hilo2.start()
	#hilo3.start()
	#hilo4.start()


def detectar_y_grabar(index, Cam, folder_temp_direc, folder_thumbnail_direc, folder_videos_direc):

	video = cv2.VideoCapture(index) #Se comienza la conexion con la fuente 
	fgbg = cv2.bgsegm.createBackgroundSubtractorMOG() #calculo de fondo 

	i = 0 
	
	#Formato para las letras (generales)
	ubicacion = (20,35)
	font = cv2.FONT_ITALIC
	tamañoLetra = 1
	colorLetra = (0,255,0)
	grosorLetra = 2

	while True:
		#Se hace la primera captura de frame
		ret, frame = video.read()	
		if ret == False: break

		#Obteniendo la resolucion de las camara
		ancho = frame.shape[1] 
		alto = frame.shape[0]
		
		#Se guarda el frame binarizado por fgbg
		fgmask = fgbg.apply(frame)
		#Varibale para saber cuantos contornos se encontraron en el frame
		area_aux_cont = 0

		#Variables auxiliares para pegar contornos en la miniatura 
		c_aux = 0
		area_aux = 0

		#Mostrar fotogramas
		cv2.imshow('fgmask',fgmask)
		cv2.imshow('Frame de afuera',frame)
		#Cuando las iteraciones superen las 30, se hace para evitar errores de deteccion
		if(i > 30):
			#Buscando contornos en el frame binarizado
			cnts, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			#Calculamos area a todos los contornos encontrados
			for c in cnts:
				area = cv2.contourArea(c)				
				print(area_aux_cont)
				#Si un area supero los 20px
				if area > 20:
					#Se aumenta el auxiliar, así descartamos el ruido en el frame
					area_aux_cont = area_aux_cont + 1
					if (area > area_aux):
						area_aux = area
						c_aux = c
			#Una vez terminado el conteo de contornos validos	
			#Si se encontraron 2 a mas contornos validos (los contornos solo aparecen cuando hay movimiento)
			#se procede a grabar 	
			if area_aux_cont >= 2:
				#Obtenemos el tiempo actual para el nombre y letras 
				now = datetime.now()
				anio = str(now.year)
				mes = str(now.month)
				dia = str(now.day)
				hora = str(now.hour)
				minuto = str(now.minute)
				segundo = str(now.second)

				#Creo las carpetas
				os.makedirs(folder_videos_direc + str(Cam) + '\\' + str(anio) + '\\' + str(datetime.strftime(now,'%b')) + '\\' + str(dia), exist_ok = True)
				os.makedirs(folder_thumbnail_direc + str(Cam) + '\\' + str(anio) + '\\' + str(datetime.strftime(now,'%b')) + '\\' + str(dia), exist_ok = True)
				#os.makedirs('c:\\Sistema_de_vigilancia_ABAE_Puerto_Cabello\\videos', exist_ok = True)

				#Formateamos el nombre del video
				full_nombre = "Cam" + str(Cam)+ " " + anio + "_" + mes + "_" + dia + "  " + hora + "_" + minuto + "_" + segundo
				direc_y_nombre_video = folder_videos_direc + str(Cam) + '\\' + str(anio) + '\\' + str(datetime.strftime(now,'%b')) + '\\' + str(dia) + '\\' + full_nombre + '.mp4'
				salida = cv2.VideoWriter(direc_y_nombre_video, cv2.VideoWriter_fourcc(*'mp4v'), 30, (ancho, alto))

				#Variables para la grabación
				i_g = 0
				t = 5 #Aca se expresa cuantos segundos quieres que dure el video 
				cv2.destroyAllWindows()
				while (True):				
					#Obtenemos frames
					ret, frame_g = video.read()
					#Estandarizacion de frames a 1280x720
					#imageOut_g = cv2.resize(frame_g,(960,720), interpolation=cv2.INTER_NEAREST)
					#frame_g = imageOut_g

					#Continuamos guardando el fondo para no perder la continuidad 
					fgmask = fgbg.apply(frame_g)
					#Obtenemos el tiempo pero esta vez es para fundirle la fecha al video
					now = datetime.now()
					anio = str(now.year)
					mes = str(now.month)
					dia = str(now.day)
					hora = str(now.hour)
					minuto = str(now.minute)
					segundo = str(now.second)
					#Se funde la fecha 
					cv2.putText(frame_g, "Cam" + str(Cam)+ " " + dia + "/" + mes + "/" + anio + "  " + hora + ":" + minuto + ":" + segundo , ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
					cv2.imshow('Frame de adentro',frame_g)
					cv2.imshow('fgmaskde adentro',fgmask)
					#Escribimos el video
					salida.write(frame_g)
					#Si estamos en la primera iteracion, guarda la miniatura
					if (i_g == 0):
						#Copiamos el frame que se guardó en el video
						thumbnail = frame_g
						#Obtenemos las coordenadas del contorno mas grande q se detectado
						x,y,w,h = cv2.boundingRect(c_aux)
						#Asignamos la miniatura en una carpeta temporal
						direc_y_nombre_miniatura = folder_temp_direc + str(Cam) + '\\' + full_nombre + '.jpg'
						#Le fundimos un cuadrado alrededor del contorno encontrado
						cv2.rectangle(thumbnail, (x,y), (x+(w+150),y+(h+150)),(0,255,0),2)
						#Guardamos en dicha carpeta
						cv2.imwrite(direc_y_nombre_miniatura , thumbnail)		
								
					i_g = i_g + 1
					#terminar video y guardar en base de datos
					if (i_g == 30*t):
						#Mover la miniatura de la carpeta temporal a su destino final
						shutil.move(folder_temp_direc + str(Cam) + '\\' + full_nombre + '.jpg', folder_thumbnail_direc + str(Cam) + '\\' + str(anio) + '\\' + str(datetime.strftime(now,'%b')) + '\\' + str(dia) + '\\' + full_nombre + '.jpg')
						#Actualizar la direccion de la miniatura						
						direc_y_nombre_miniatura = folder_thumbnail_direc + str(Cam) + '\\' + str(anio) + '\\' + str(datetime.strftime(now,'%b')) + '\\' + str(dia) + '\\' + full_nombre + '.jpg'
						#Registramos en la base de datos todo sobre el video
#Insertar base de datos #BD_MobB.insertar_video(full_nombre + '.mp4', now, direc_y_nombre_video, direc_y_nombre_miniatura,'' )
						#reseteamos la variable que detona la grabacion
						area_aux_cont = 0
						#Rompemos la grabacion
						break
					cv2.waitKey(15)
				#cerramos la camara de grabacion
				cv2.destroyAllWindows()
				salida.release()
			#Esto es una medida de seguridad, para que i no crezca tanto
			#y este no alcance así su maximo, ya que si el sistema pasa mucho 
			#tiempo corriendo, eventualmente se alcanzaria este limite
			i = 40
		i = i+1
		cv2.waitKey(15)
	video.release()


main()
