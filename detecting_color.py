import cv2
import numpy as np
def empty(x=90):
    pass
img = cv2.imread('C:/Users/Asus/Downloads/lambo.png')
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars',640,240)   #TrackBars is the name of the window
cv2.createTrackbar('hue Min','TrackBars',0,179,empty)  #hue Min is the name of the track bar.you can use any name.empty is the function that execute every time if user changes th trackbar
#0 is the minimum value and 179(count from 0) is the maximum angle it is 180 if you count from 1
cv2.createTrackbar('hue Min','TrackBars',0,179,empty)
cv2.createTrackbar('hue Max','TrackBars',179,179,empty)
cv2.createTrackbar('Sat Min','TrackBars',0,255,empty)
cv2.createTrackbar('Sat Min','TrackBars',255,255,empty)
cv2.createTrackbar('Val Min','TrackBars',0,255,empty)
cv2.createTrackbar('Val Min','TrackBars',255,255,empty)

imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h_min = cv2.getTrackbarPos('hue Min','TrackBars')
cv2.imshow("Original",img)
cv2.imshow("HSV",imgHSV)
cv2.waitKey(0)
