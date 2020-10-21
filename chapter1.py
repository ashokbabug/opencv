import cv2
# print('pakage imported')
# img = cv2.imread('D:/photos/wallpapers/kajal.jpg') # it takes the image and return as multi-dimensional numpy array
# cv2.imshow('output',img)   #output is the name of the window ang img is yhe image
# cv2.waitKey(0)  #0 means infinite delay and any value means that the delay is that many ms
# video capturing
# cap = cv2.VideoCapture('D:/videos/MindBlock.mp4')
# while True:
#     success,img = cap.read()  #success is a boolean value it tells whether the image is loaded successfullt or not
#     cv2.imshow('Video',img)
#     if cv2.waitKey(240) & 0xFF == ord('q'):
#         break
# web cam
cap = cv2.VideoCapture(0)
# every property has a number associated with it eg.3 for width 4 for height
cap.set(3, 640)  # id number 3 with width 640
cap.set(4, 480)  # id number 4 with height 480
cap.set(10, 100)  # id for setting brightness is 10
while True:
    # success is a boolean value it tells whether the image is loaded successfullt or not
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(240) & 0xFF == ord('q'):
        break
