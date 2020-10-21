import cv2
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 640)  # id number 3 with width 640
cap.set(4, 480)  # id number 4 with height 480
print(cap.get(3))
print(cap.get(4))
cap.set(10, 100)  # id for setting brightness is 10
while True:
    # success is a boolean value it tells whether the image is loaded successfullt or not
    success, img = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    date = str(datetime.datetime.now())
    text = 'Width: '+str(cap.get(3))+' Heigth: '+str(cap.get(4))+date
    # 1 is for font scale .2 is for thickness
    frame = cv2.putText(img, text, (10, 50), font, 1,
                        (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('Video', img)
    if cv2.waitKey(240) & 0xFF == ord('q'):
        break
