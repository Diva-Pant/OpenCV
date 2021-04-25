import cv2 as cv
import numpy as np

img = cv.imread("Photos/cutecat.jpg")
def rescaleFrame(frame, scale=0.20):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

#Translation
def translate(resized_image,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(resized_image.shape[1],resized_image.shape[0])
    return cv.warpAffine(resized_image,transMat,dimensions)
# -x : shift left, -y : shift up
#x : shift right, y : shift down

translated = translate(resized_image, -100,100)
cv.imshow('Translated', translated)

#Rotation
def rotate(resized_image,angle,rotPoint=None):
    (height,width)=resized_image.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)

    rotMat=cv.getRotationMatrix2D(rotPoint, angle,1.0)
    dimensions=(width,height)

    return cv.warpAffine(resized_image,rotMat,dimensions)

rotated = rotate(resized_image,45)
cv.imshow("Rotated", rotated)

#Flipping

flip =cv.flip(resized_image,-1)
cv.imshow('Flip',flip)

#Cropping
cropped= img[200:400,300:400]
cv.imshow('Crop', cropped)

cv.waitKey(0)
