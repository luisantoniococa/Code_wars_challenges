import cv2
import numpy as np

# creates an image in the rbg scale thanks to the np.uint8

img = np.zeros((512,512,3), np.uint8)

# print(img)
# img[:] = 255,0,0 # this last part tells the color we want to create

# now we are going to create a line
# we need to add  a starting point, ending point and a color also the thinkness
cv2.line(img,(0,0),(300,90), (0,255,0),3)

cv2.imshow('Image', img)

cv2.waitKey(0)