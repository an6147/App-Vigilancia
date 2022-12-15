import cv2
import numpy as np
from datetime import datetime
import time
import threading

def main():

	index1 = "http://192.168.1.6:4747/video"
	index2 = "http://192.168.1.2:4747/video"
	index3 = 0
	

	hilo1 = threading.Thread(target = detectar_y_grabar, args = (index1, 1,))
	hilo2 = threading.Thread(target = detectar_y_grabar, args = (index2, 2,))
	#hilo3 = threading.Thread(target = detectar_y_grabar, args = (index3, 3,))

	hilo1.start()
	hilo2.start()
	#hilo3.start()


def detectar_y_grabar(index, Cam):

	video = cv2.VideoCapture(index) 
	fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
	i = 0
	
	ubicacion = (20,35)
	font = cv2.FONT_ITALIC
	tamañoLetra = 1
	colorLetra = (0,255,0)
	grosorLetra = 2

	while True:
		ret, frame = video.read()	
		if ret == False: break
		fgmask = fgbg.apply(frame)
		
		now = datetime.now()
		anio = str(now.year)
		mes = str(now.month)
		dia = str(now.day)
		hora = str(now.hour)
		minuto = str(now.minute)
		segundo = str(now.second)

		# Para OpenCV 4
		cnts, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		#cv2.drawContours(frame, cnts, -1, (0,0,255),2)

		#cv2.imshow('fgmask',fgmask)
		#cv2.putText(frame, dia + "/" + mes + "/" + anio + "  " + hora + ":" + minuto + ":" + segundo , ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
		#cv2.imshow('Frame de afuera',frame)

		if(i>30):
			for c in cnts:
				area = cv2.contourArea(c)

				#print(area)
				if area > 50:
					#x,y,w,h = cv2.boundingRect(c)
					#cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),2)
					now = datetime.now()
					anio = str(now.year)
					mes = str(now.month)
					dia = str(now.day)
					hora = str(now.hour)
					minuto = str(now.minute)
					segundo = str(now.second)

					full = "Cam" + str(Cam)+ " " + anio + "_" + mes + "_" + dia + "  " + hora + "_" + minuto + "_" + segundo + ".mp4" #conversion a texto 
					#full= full.replace( ':', '_') #sustitucion de ":" por "_" que si son aceptados en los nombres 
					salida = cv2.VideoWriter(full, cv2.VideoWriter_fourcc(*'mp4v'), 30, (640,480))

					i_g = 0
					t = 5
					#cv2.destroyAllWindows()
					while (True):				
						#Usar write para GUARDAR el video
						ret, frame_g = video.read()
						fgmask = fgbg.apply(frame_g)
						now = datetime.now()
						anio = str(now.year)
						mes = str(now.month)
						dia = str(now.day)
						hora = str(now.hour)
						minuto = str(now.minute)
						segundo = str(now.second)
						cv2.putText(frame_g, "Cam" + str(Cam)+ " " + dia + "/" + mes + "/" + anio + "  " + hora + ":" + minuto + ":" + segundo , ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
						#cv2.imshow('Frame de adentro',frame_g)
						#cv2.imshow('fgmaskde adentro',fgmask)					
						salida.write(frame_g)
						i_g = i_g+1
						if (i_g == 30*t):
							break

					#cv2.destroyAllWindows()
					salida.release()
					ret, frame = video.read()		

		i = i+1
	video.release()

main()
