import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0) 

while(True):
	ret, frame = cap.read()
	display = frame.copy()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray,(5,5),0);
	gray = cv2.medianBlur(gray,5)

	gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,3.5)
	
	circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1, 260, param1=30, param2=65)
	
	
	if circles is not None:
		circles = np.round(circles[0, :]).astype("int")
		
		for (x, y, r) in circles:
			
			cv2.circle(display, (x, y), r, (0, 0, 0), 4)
			cv2.circle(display, (x,y),2,(255,255,255),-1)
			
    	cv2.imshow('frame',display)
 	if cv2.waitKey(1) & 0xFF == ord('s'):
		break
cap.release()
cv2.destroyAllWindows()