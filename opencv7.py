import cv2
print(cv2.__version__)
dispW=640
dispH=580
flip=2
#Uncomment These next Two Line for Pi Camera
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam= cv2.VideoCapture(camSet)
 
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
def nothing(x):
    pass
cam=cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
cv2.namedWindow('nanoCam')
cv2.createTrackbar('xVal','nanoCam',15,dispW,nothing)
cv2.createTrackbar('yVal','nanoCam',15,dispH,nothing)
cv2.createTrackbar('width','nanoCam',15,dispH,nothing)
cv2.createTrackbar('height','nanoCam',15,dispH,nothing)
while True:
    ret, frame = cam.read()
    xValue=cv2.getTrackbarPos('xVal','nanoCam')
    yValue=cv2.getTrackbarPos('yVal','nanoCam')
    wid=cv2.getTrackbarPos('width','nanoCam')
    hght=cv2.getTrackbarPos('height','nanoCam')
    frame=cv2.rectangle(frame,(xValue,yValue),(xValue+wid,yValue+hght),(255,0,0),2)
    #cv2.circle(frame,(xValue,yValue),5,(255,0,0),-1)
    
    print(xValue)
    print(yValue)
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',720,0)
    
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()