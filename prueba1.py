import cv2
import numpy as np
cam = cv2.VideoCapture(0)
kernel = np.ones((5,5),np.uint8)

while (True):
	ret,frame = cam.read()
	rangomax = np.array([30,30,30])
	rangomin = np.array([0,0,0])
	mascara = cv2.inRange(frame, rangomin, rangomax)
	#Eliminamos ruido MORPH_OPEN.
	opening = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
	x,y,w,h = cv2.boundingRect(opening)
	gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gris = cv2.GaussianBlur(frame, (21, 21), 0)
	cv2.rectangle(gris,(x,y),(x+w,y+h),(0,255,0),4)
	cv2.circle(gris,(x+w/2,y+h/2),6,(0,0,100),-1)
	#Mostramos imagen en camara
	cv2.imshow('Prueba 1' ,frame)
	#Prueba
	#gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('EscalagRIS' ,gris)

	k = cv2.waitKey(1) & 0xFF
	if k==ord("s"):
		break
