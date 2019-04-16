import cv2
import imutils
import numpy as np

result = False

img = cv2.imread('in_memory_to_disk2.png')
img = imutils.resize(img, width=600)
img3 = img[97:178,180:274]

cv2.imshow('window', img3)
#cv2.imshow('window2',giratina)

#cv2.waitKey(0)
#cv2.destroyAllWindows()"""

img2 = cv2.imread('Screenshot2.png')
img1 = cv2.imread('Screenshot1.png')
img0 = cv2.imread('Screenshot0.png')

d1 = cv2.subtract(img0, img1)
d2 = cv2.subtract(img0, img2)
d3 = cv2.subtract(img1, img2)
d4 = cv2.subtract(img1, img3)

cv2.imshow('window1', img2)
cv2.imshow('window2', img1)
cv2.imshow('window4', img0)


if result is True:
    print ("Pictures are the same")
print(not np.any(d1))
print(not np.any(d2))
print(not np.any(d3))
print(not np.any(d4))
cv2.waitKey(0)
cv2.destroyAllWindows()
