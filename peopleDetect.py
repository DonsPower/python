from __future__ import print_function
from imutils.object_detection import non_max_suppression
import numpy as np
import cv2
import imutils
# Capture video from file
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret == True:
        #Reduce la imagen para el mejor análisis
        frame = imutils.resize(frame, width=min(476, frame.shape[1]))
        #init HOG
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        #Detect people in the video
        (rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4),
                                                padding=(8, 8), scale=1.05)
        for (x, y, w, h) in rects:
    		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

         # draw the final bounding boxes
        for (xA, yA, xB, yB) in pick:
                     cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
        cv2.imshow('frame',frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
