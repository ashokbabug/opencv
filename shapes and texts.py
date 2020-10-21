
img = np.zeros((512,512,3),np.uint8)
# img[200:300,100:300] = 255,0,0   #to make a part into blue color
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),thickness=3)  #here 3 is the thickness
cv2.rectangle(img,(100,100),(300,450),(0,0,255),cv2.FILLED)  #cv2.filled fill the rectangle with the given color
cv2.circle(img,(100,100),30,(255,255,0),thickness=2)
cv2.putText(img,"OPEN CV",(30,400),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),thickness=2)  #here 1 is the scale(size)
cv2.imshow('Image',img)
print(img.shape)
cv2.waitKey(0)