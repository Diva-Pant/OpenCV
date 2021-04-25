import cv2 as cv

img = cv.imread('Photos/cat.jpg')

def rescaleFrame(frame, scale=0.20):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img)
#cv.imshow('Image', resized_image)
#Converting image to grayscale
#gray = cv.cvtColor(resized_image,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)
#Blurring images
blur = cv.GaussianBlur(resized_image,(3,3), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Cascade
canny = cv. Canny(resized_image,125,175)
cv.imshow('Canny Edges', canny)

#Dilating the image(smoothing the image after edge detection, noise removal)
dilated = cv.dilate(canny,(3,3), iterations=3)
cv.imshow("Dilated", dilated)

#Eroding (to get the edges back as the original almost)
eroded= cv.erode(dilated,(3,3),iterations=1)
cv.imshow("Eroded", eroded)

#Resize images
resized=cv.resize(resized_image,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#Cropping
cropped=resized_image[50:200,300:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
