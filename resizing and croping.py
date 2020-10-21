import cv2
import numpy as np
img = cv2.imread('D:/photos/wallpapers/sam.jpg')
print(img.shape)
# imdResize = img.resize(img,(1500,1200))   #not working
imgCropped = img[0:200,200:500]  #height is 0:200 width is 200:500
cv2.imshow('output',img)
cv2.imshow('Cropped Image',imgCropped)
cv2.waitKey(0)