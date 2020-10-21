import cv2 as cv
import numpy as np
img = cv.imread('lambo.png',0)

cv.imshow('Image',img)
cv.waitKey(0)
cv.destroyAllWindows()