import numpy as np
import cv2
# x is the curent position of the trackbar
def nothing(x):
    print(x)
img = np.zeros((250,500,3),np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('trackbarname','image',0,255,nothing)
cv2.createTrackbar('trackbarname2','image',0,255,nothing)
cv2.createTrackbar('trackbarname3','image',0,255,nothing)
switch = '0 : OFF \n 1 : ON'
cv2.createTrackbar(switch,'image',0,1,nothing);

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    b = cv2.getTrackbarPos('trackbarname','image')
    g = cv2.getTrackbarPos('trackbarname2', 'image')
    r = cv2.getTrackbarPos('trackbarname3', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()






# import numpy as np
# import cv2 as cv
#
# def nothing(x):
#     print(x)
#
# # Create a black image, a window
# img = np.zeros((300,512,3), np.uint8)
# cv.namedWindow('image')
#
# cv.createTrackbar('B', 'image', 0, 255, nothing)
# cv.createTrackbar('G', 'image', 0, 255, nothing)
# cv.createTrackbar('R', 'image', 0, 255, nothing)
#
# while(1):
#     cv.imshow('image',img)
#     k = cv.waitKey(1) & 0xFF
#     if k == 27:
#         break
#
#     b = cv.getTrackbarPos('B', 'image')
#     g = cv.getTrackbarPos('G', 'image')
#     r = cv.getTrackbarPos('R', 'image')
#     img[:] = [b, g, r]
#
#
#
#
# cv.destroyAllWindows()