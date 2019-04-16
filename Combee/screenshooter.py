import numpy as np
import pyautogui
from pynput.keyboard import Key, Controller
import imutils
import cv2
import time

keyboard = Controller()
with keyboard.pressed(Key.cmd_r):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

time.sleep(2)

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("encounter_screen.png", image)
image = imutils.resize(image, width=600)
combee = image[97:178,180:274]
cv2.imwrite("referencefemale.png", combee)
