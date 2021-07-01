import cv2
img=cv2.imread('E:\DIP\opencv\opencv-master\opencv-master\samples\data\lena.jpg',1)
print(img)
cv2.imshow('image',img)
k=cv2.waitKey()
if k==27:
    cv2.destroyAllWindows()
elif k==ord('a'):
    cv2.imwrite('E:\DIP\opencv\opencv-master\opencv-master\samples\data\lenaedited.png',img)