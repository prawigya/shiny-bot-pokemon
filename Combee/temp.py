import cv2
import imutils
import numpy as np

result = False

img = cv2.imread('reference.png')
img2 = cv2.imread('referencefemale.png')




d1 = cv2.subtract(img, img2)

print(not np.any(d1))
