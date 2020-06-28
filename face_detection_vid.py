import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
# cap = cv2.VideoCapture(0)
# To use a video file as input 
cap = cv2.VideoCapture("corres_filename.mp4")

while True:
    # Read the frame
    # Here the first parameter is not mandatory and so it is scripted underscore which means nothing.
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 10)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2)
        #cv2.putText(img, "Santhosh", (x+12,y-12),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),2)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    # As ASCII Value of ESC is 27
    if(cv2.waitKey(1) & 0xff) == 27:
        break
        
#As it is a video, the frames being recorded needs to be released
cap.release()
