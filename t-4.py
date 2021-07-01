import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('outputt5.avi',fourcc,30.0,(640,480))
while (True):
    ret,frame=cap.read()
    if ret==True:
        out.write(frame)
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('myframe',frame)
        if cv2.waitKey(1)& 0xff==ord('q'):
            break;
    else:
        break;
cap.release()
out.release()
cv2.destroyAllWindows()