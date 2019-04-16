import time
from pynput.keyboard import Key, Controller
import functions as fn
import cv2

non_shiny1 = cv2.imread('referencemale_night.png')
non_shiny2 = cv2.imread('referencefemale_night.png')

keyboard = Controller()
c = 0
#Switching tabs and getting to Desmume
with keyboard.pressed(Key.cmd_r):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

time.sleep(2)
with keyboard.pressed(Key.space):
    while True:
        fn.encounter_pkmn()
        time.sleep(2.5)
        if(fn.isShiny(non_shiny1, non_shiny2)):
            #Code when shiny pokemon is encountered
            keyboard. press('k')
            time.sleep(0.5)
            keyboard.release('k')
            print("Shiny pokemon encountered after ",c+1,"encounters")
            time.sleep(1)
            break
        c+=1
        print("Not Shiny, Encounter: ",c)
        fn.reset_reload()
        time.sleep(0.5)
