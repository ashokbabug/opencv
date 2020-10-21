# Thresholding is a popular segmentation technique used for seperation an object from its baclground
# we compare each pixel of an image with a predefined threshold value.it divides all the pixels of the image into 2 groups
# first group have the intensity value grater than the threshold value and other have less intensity
import cv2 as cv
import numpy as np
img = cv.imread('gradient.png', 0)
# if the value of the pixel is less than 127 then it will become 0 and if grater it will become 255
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# inverse of THRESH_BINARY
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
# upto 127 the pixel values donot change after 127 the ppixel value is 127 only
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

cv.imshow('Image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)
cv.waitKey(0)
cv.destroyAllWindows()
