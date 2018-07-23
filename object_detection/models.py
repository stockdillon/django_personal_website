from django.db import models
import cv2 as cv
import os

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(null=True, blank=True)


class Result(models.Model):
    objects = models.Manager() # This was added to prevent a pylint warning in VSC... not necessary
    filename = models.CharField(max_length=100)
    image = models.ImageField(height_field=0, width_field=0)

    def process(self):
        print(" ----- PROCESSING -----")
        #print(self.image.url)
        #print(os.listdir())
        url = "object_detection/" + self.image.url
        print(f"Joined URL: {url}")
        #img = cv.imread(url, cv.IMREAD_COLOR)
        face_cascade = cv.CascadeClassifier('object_detection/haarcascade_frontalface_default.xml')
        eye_cascade = cv.CascadeClassifier('object_detection/haarcascade_eye.xml')

        img = cv.imread(url)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            
            #for (ex,ey,ew,eh) in eyes:
            #    cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
        cv.imwrite(url, img)
        #cv.imshow('img',img)
        #cv.waitKey(0)
        #cv.destroyAllWindows()