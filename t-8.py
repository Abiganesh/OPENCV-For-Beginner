import cv2
def click_event(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,'',y)
        font=cv2.FONT_HERSHEY_TRIPLEX
        message= str(x)+' '+str(y)
        cv2.putText(img,message, (x,y),font,0.5,(251,125,10),2)
        cv2.imshow('image',img)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv2.FONT_HERSHEY_TRIPLEX
        font=cv2.FONT_HERSHEY_TRIPLEX
        message= str(blue)+str(green)+str(red)
        cv2.putText(img,message, (x,y),font,0.5,(251,125,10),2)
        cv2.imshow('image',img)
img=cv2.imread('E:\DIP\opencv\opencv-master\opencv-master\samples\data\lena.jpg',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()