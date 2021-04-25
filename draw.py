import cv2 as cv
import numpy as np

#Creating blank images
blank = np.zeros((500,500,3), dtype = 'uint8')
#cv.imshow('Blank', blank)
# 1.Paint the image a certain color
#blank[:] = 0,255,0
#cv.imshow('Green', blank)
# 2. Paint certain portion of images
#blank[200:300,300:400] = 0,255,0

#3. Draw the rectangle
#cv.rectangle(blank,(0,0),(250,250), (0,255,0), thickness=2)
#cv.imshow('Rectangle', blank)
#4. Playing with the parameters
#cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=3)
#cv.imshow('Rectangle', blank)
#5. Not giving the absolute values
#cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,255,0))
#cv.imshow('Rectangle', blank)
#6. Draw a circle
#cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255), thickness=4)
#cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255), thickness=-1)
#cv.imshow('Circle', blank)
#7. Draw a line
cv.line(blank,(100,200),(300,400),(255,255,255),thickness=5)
cv.imshow('Line', blank)
#8. Write text on images
cv.putText(blank, 'Hello opencv', (255,255), cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text', blank)
#Using the image from the computer
#img = cv.imread('Photos/cat.jpg')
#cv.imshow('Cat',img)
cv.waitKey(0)
