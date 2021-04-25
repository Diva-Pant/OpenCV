import cv2 as cv
import numpy as np
img = cv.imread('Photos/cutecat.jpg')


def rescaleFrame(frame, scale=0.20):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)
#Drawing contours on blank image
blank = np.zeros(resized_image,dtype='uint8')
cv.imshow('Blank', blank)

#Converting to grayscale
gray=cv.cvtColor(resized_image,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
blur=cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur,125,175)
cv.imshow('Canny Edges', canny)
#Threshold instead of canny to find Contours
#ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
#cv.imshow("Threshold",thresh)

contours,hierarchies = cv.findContours(thresh, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow("Contours drawn on blank", blank)

cv.waitKey(0)
