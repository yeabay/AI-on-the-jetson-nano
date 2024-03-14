import cv2
print(cv2.__version__)
dispW=620
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
    
    frame=cv2.rectangle(frame,(x,y),(x+width,y+height),(255,0,0),-1)
    #frame=cv2.circle(frame,(320,240),50,(255,0,0),4)
    #fnt=cv2.FONT_HERSHEY_DUPLEX
    #frame=cv2.putText(frame,'My First Text',(300,300),fnt,1,(255,0,150), 2)
    #frame=cv2.line(frame,(10,10),(630,470),(0,0,0),4)
    #frame=cv2.arrowedLine(frame, (10,470),(630,10),(0,0,0),4)

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()