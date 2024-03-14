import cv2
import numpy as np
print(cv2.__version__)
dispW=640
dispH=480
flip=2
evt=-1
cord=[]

img =np.zeros((250,250,3),np.uint8)
def click(event,x,y,flag, params):

    global pnt
    global evt

    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event Was: ' ,event)
        print(x,',',y)
        pnt=(x,y)
        cord.append(pnt)
        print(cord)
        evt=event
    if event==cv2.EVENT_RBUTTONDOWN:
        print(x,y)
        blue=frame[y,x,0] 
        green=frame[y,x,1] 
        red=frame[y,x,2] 
        print(blue,green,red)
        colorString=str(blue)+','+str(green)+','+str(red)
        img[:]=[blue,green,red]
        fnt=cv2.FONT_HERSHEY_PLAIN
        r=255-int(red)
        g=255-int(green)
        b=255-int(blue)
        tp=(b,g,r)
        cv2.putText(img, colorString,(10,25),fnt,1,tp,2)
        cv2.imshow('mycolor',img)
cv2.namedWindow('nanoCam')
cv2.setMouseCallback('nanoCam',click)
#Uncomment These next Two Line for Pi Camera
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam= cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
cam=cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
while True:
    ret, frame = cam.read()
    for nts in cord:
        cv2.circle(frame,nts,2,(0,0,255),-1)
        font =cv2.FONT_HERSHEY_SIMPLEX
        mystr=str(nts)
        cv2.putText(frame,mystr,nts,font,0.5,(255,0,0),1)

    '''if evt==1:
        cv2.circle(frame,pnt,5,(0,0,255),-1)
        font =cv2.FONT_HERSHEY_SIMPLEX
        mystr=str(pnt)
        cv2.putText(frame,mystr,pnt,font,1,(255,0,0),2)'''
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,260)
    
    keyEvent=cv2.waitKey(1)
    if keyEvent==ord('q'):
        break
    if keyEvent==ord('c'):
        cord=[]
cam.release()
cv2.destroyAllWindows()