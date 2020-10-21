import numpy as np
import cv2




def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # cv2.circle(img,(x,y),2,(0,0,255),-1)  #-1 is the thickness.if it is -1 it fill the empty space
        # points.append((x,y))
        # if len(points) >= 2:
        #     cv2.line(img,points[-1],points[-2],(255,0,0),4)
        # cv2.imshow('image',img)
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorimage = np.zeros((512,512,3),np.uint8)
        mycolorimage[:] = [blue,green,red]
        cv2.imshow('color',mycolorimage)


# img = np.zeros((512,512,3),np.uint8)
img =cv2.imread('lambo.png')
cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()