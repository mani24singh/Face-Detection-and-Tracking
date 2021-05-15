import cv2

alg= "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture('http://192.168.43.1:4747/video')
count=1
while True:
    _,img=cam.read()
    grayImg= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face=haar_cascade.detectMultiScale(grayImg,1.3,4)
    if face==():
        print("no person detected")
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        print("person detected {}".format(count))
        count+=1
    cv2.imshow("FaceDetection",img)
    key=cv2.waitKey(10)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()
