import cv2
import numpy as np


# crop an image

img = cv2.imread("th2.jpg")
y=0
x=0
h=100
w=200
crop_img = img[y:y+h, x:x+w]
cv2.imshow("Image", crop_img)
cv2.waitKey(0)
#cv2.imwrite('crop1.jpg', crop_img)