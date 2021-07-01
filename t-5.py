import cv2
import numpy as np
img=cv2.imread('E:\DIP\opencv\opencv-master\opencv-master\samples\data\lena.jpg',1)
img=np.zeros([512,512,3],np.uint8)
img=cv2.line(img,(0,0),(255,255),(245,45,250),5)
img=cv2.arrowedLine(img,(0,10),(255,255),(245,0,250),5)
img=cv2.rectangle(img,(20,0),(255,255),(205,45,250),5)
img=cv2.circle(img,(20,0),63,(245,45,20),5)
font=cv2.FONT_ITALIC
img=cv2.putText(img,'lena',(10,50),font,4,(0,15,35),5,cv2.LINE_AA)
cv2.imshow('image',img)
k=cv2.waitKey()
if k==27:
    cv2.destroyAllWindows()
