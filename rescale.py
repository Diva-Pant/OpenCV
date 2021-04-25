import cv2 as cv
#Reading images
img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat',img)
def rescaleFrame(frame, scale=0.20):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
#Reading videos
capture = cv.VideoCapture('Videos/friend.mp4')

while True:
    isTrue, frame = capture.read()
    resized_frame = rescaleFrame(frame, scale=0.5)

    cv.imshow('Video', frame)
    cv.imshow('Resized Video', resized_frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)
cv.waitKey(0)

#Changing Resolution of the videos
#def changeRes(width,height):
    #Works only for live videos not the standalone video files
    #capture.set(3,width)
    #capture.set(4,height)
