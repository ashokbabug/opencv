import cv2
import numpy as np
img = cv2.imread('C:/Users/Asus/Downloads/cards.jpg')

# imgHor = np.hstack((img,img))  #both of the images in the stack should have the same no of chanels
# imgVer = np.vstack((img,img))
# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)
# cv2.waitKey(0)