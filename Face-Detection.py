import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

count=1
while count < 100:
    print(count)
    (_, img) = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        count=count+1
    cv2.imshow('FaceDetection',img)
    key = cv2.waitKey(10)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()
