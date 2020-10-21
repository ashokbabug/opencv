import cv2
import numpy as np
kernal = np.ones((5,5),np.uint8)
img = cv2.imread('D:/photos/wallpapers/sam.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #to convert  image into gray scale
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)   #ksize is kernal size it should be as (odd_num,odd_num)
imgCanny = cv2.Canny(img,100,100)
imgDialation = cv2.dilate(imgCanny,kernal,iterations=1)
imgEroded = cv2.erode(imgDialation,kernal,iterations=1)
cv2.imshow("Gray Image",imgGray)
cv2.imshow('Blur Image',imgBlur)
cv2.imshow('canny Image',imgCanny)
cv2.imshow('Dialation Image',imgDialation)
cv2.imshow('Eroded Image',imgEroded)
cv2.waitKey(0)