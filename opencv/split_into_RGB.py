import cv2
import numpy as np


# split image into three RGB channel images

img = cv2.imread("th2.jpg")
b,g,r = cv2.split(img)
cv2.imwrite('blue_channel.jpg', b)
cv2.imwrite('green_channel.jpg', g)
cv2.imwrite('red_channel.jpg', r)