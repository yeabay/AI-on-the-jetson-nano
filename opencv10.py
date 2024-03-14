import cv2
print(cv2.__version__)
dispW=680
dispH=540
flip=2
#Uncomment These next Two Line for Pi Camera
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam= cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
cam=cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
x=140
y=100
width=100
height=100
vx=2
vy=2
while True:
    ret, frame = cam.read()
    x+=vx
    y+=vy

    if x<=0 or x+width >=dispW:
        vx=-vx
    if y<=0 or y+height>=dispH:
        vy=-vy
    
   
    
    roi=frame[y:y+height,x:x+width]
    Gframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    roiGray=cv2.cvtColor(Gframe,cv2.COLOR_GRAY2BGR)
    frame=cv2.rectangle(roiGray,(x,y),(x+width,y+height),(0,0,255),2)
    #roiGray=cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)
    roiGray[y:y+height,x:x+width]=roi
   
    #cv2.imshow('Gray',roiGray)
    cv2.imshow('nanoCam',roiGray)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()