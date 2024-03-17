import cv2 
import numpy as np

sift = cv2.SIFT_create()

vid = cv2.VideoCapture(0)

while True:

	ret,frame = vid.read()

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	kp = sift.detect(gray, None)

	img = cv2.drawKeypoints(frame,kp,frame) #flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS

	cv2.imshow('bookscan',img)

	if cv2.waitKey(1) == ord('q'):
		break

vid.release()

cv2.destroyAllWindows()