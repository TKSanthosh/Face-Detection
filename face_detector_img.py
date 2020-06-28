import cv2

face_cascade_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('msdhoni.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces_avail = face_cascade_model.detectMultiScale(gray, 1.1, 5)

for (x, y, w, h) in faces_avail:
    cv2.rectangle(image, (x, y), (x + w, y + h), (200,20,60), 3)
    
cv2.imshow('image', image)
'''Wait key takes the seconds (in ms) as parameter
#false indicates that image to be present forever 
#true indicates that image to show only for 1 sec as true implys the value '1''''
cv2.waitKey(False)

#The code is small right.!? That is because it is all about the Casecade Classifier(dataset) that is used within this, which is a haarcascade. :-)
