import numpy as np
import cv2
img1 = np.zeros((250,500,3),np.uint8)
cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = np.ones((250,500,3),np.uint8)
bitAnd = cv2.bitwise_and(img2,img1)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('bitAnd',bitAnd)
cv2.waitKey(0)
cv2.destroyAllWindows()

#bitwise operators are used when you are working with masks(masks are binary imges  inwhich an operation is to be performed)
