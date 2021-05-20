# Shiny Bot
Python script that automates Shiny Hunting of Pokemon in DS/ GBA emulators.

A Shiny Pokemon is one who's sprite has a different color scheme than it's original, and produces a sparkly LED sequence when released from a Pokeball or encountered. Shiny Pokemon have very rare encounter rates in the game. (1 in 8192 to be precise in games up till Generation 4).
Players spend hours Shiny Hunting Pokemon, and are successful after thousands of random encounters (RE). The task can however, be automated using a Python script, which can give a certain set of commands in the keyboard such that the game soft resets itself until it encounters a Shiny.

This repository contains a script that can automate the task of soft-resetting the game until a Shiny is encountered.
The script has been tested and works successfully.


<p align="center">
  <img src="https://media.giphy.com/media/ekeaFiuGDE2vdIqfIy/giphy.gif">
</p>

After encountering the Shiny Pokemon, the Loop breaks and saves state into the emulator. The pokemon can then be caught and you finally end up with a Shiny.


<div class="row">
  <div class="column">
    <img src="Images/Combee.png" alt="Snow" style="width:100%">
  </div>
</div>

# Working

The script controls your keyboard and presses keys in intervals to automate the shiny hunting process. It triggers an encounter and takes a screenshot of the encountered Pokemon. The encountered screenshot is compared with a saved encounter screenshot of the Pokemon. If the two encounters do not match, then it is a shiny. If they do match, then it is not a shiny and the process loops again. 

## Note
This version of the script only works for static encounters, i.e., you need to press A to trigger the encounter. For Pokemon DPPt, this includes legendary pokemon, trees slathered with honey, starters, Drifloon on the Windworks and other such encounters. 


## Emulator settings
The keyboard controls of the emulator is configured in the following manner:
(Keyboard Key : Action)

z : A on the NintendoDS

k : Quicksave

i : Soft Reset the game

Space Bar: Speedup x4

(These are the only keys you need to run the script successfully)

### Position in the game
In the game, you need to be standing in such a position that pressing A will trigger the encounter. Save the game in that position and you're all set. By doing so, if you press A immediately after soft resetting, the encounter is triggered (check the GIF)

## Setting up the script
Use the Combee directory as reference to the following scripts.
The following steps are required for you to set up the Shiny Hunter: 
1. Edit screenshooter.py code 
2. Run screenshooter.py
3. Edit functions.py if necessary
4. Run keyboard.py


### screenshooter.py: Taking a screenshot of an encounter

For this script to run, you need to open a DS emulator and a terminal. You need the terminal as the active window and set it up such that when you press Ctrl + Tab, the emulator is opened. 
The emulator must be running the game and the encounter screen should be displayed on it.
Then you run the script screenshooter.py from that terminal. The script first presses Ctrl + Tab and then takes a screenshot of the encounter screen. 

After that if crops out the image of the pokemon from the encounter screen. For this to happen accurately for your system and its monitor resolution, you need to alter line 19 of the code, where the coordinates for the encounter screen are specified. 

> combee = image[97:178,180:274]

Set up the four coordinates accordingly, you can do this by a trial and error method (by running the script, seeing the saved image and adjusting the four values), or by taking a screenshot of the screen, and seeing where the coordinates of the pixels lie. 

(Note: Try and make the area of the box as small as possible, such that the background is not included and also only the section of the Pokemon is cropped which is necessary for you to identify a shiny. If you include the background, the day and night cycles in the background can trigger a false positive)

Check your saved image, 'reference.png' (or whatever it is called) and decide if it is good enough. If you think it should do, continue with the next section, or else just adjust the coordinates and repeat.

### functions.py and keyboard.py
Running the keyboard.py script is almost same to the screenshooter.py. You need the terminal as the active window and set it up such that when you press Ctrl + Tab, the emulator is opened. You save file must be in the position specified in the position above to encounter the pokemon.

The functions in functions.py include resetting the game, encountering the pokemon, and checking if it is a shiny by comparing the screenshots.
The keyboard.py repeats the above process until a shiny is encountered.
The Space Bar is pressed at all times while the above functions are called to speedup the process. If the pressing of buttons is not in sync in your system, you can always change the time intervals in which the buttons are pressed in functions.py

Run the script a few times to check if the process occurs smoothly. If all works well then you're set to go. 

(Note: You might need to modify the script a little for encounter with every pokemon so it is suggested you create a directory for each pokemon, modify the script accordingly, and run it)
Have fun!

# FAQ
#### The script says encountered a Shiny even when it is not a shiny.
This can happen because of two reasons:
1. In Gen 4, the male and female sprites are slightly different for some pokemon. The reference image you saved can be of one gender and when you encounter pokemon of another gender it assumes it is a shiny since the sprites are different. For example female Combees have a mark on their forehead, while males do not. One way to get around it is to minimze the size of the reference screenshot so that the part that differentiates males and females are cropped out, and thus not considered. You can also use two sprites, one of male, and one of female and modify the script to consider both the genders while checking for shiny. (The script for combee uses both gender sprites as reference images whereas the Giratina script uses only one reference image as legendaries don't have genders) 
2. You have included the background in your reference image. In Gen4 you have day, evening, and night cycles and the encounter screen background also changes accordingly. If your script is running for hours and the time changes from day to night, your encounter screen will change to night, but your reference image will still have the day backgorund. Comparing the images will cause the script to return a True for differences in the image. This results in a False Positive. A fix for this is to reduce the reference image as to not include the background. (You do not have to worry for cave encounters like Giratina as the background for cave encounters do not change.)

#### Q: Why are you using a Python script and going through all this hassle when you can just use gameshark codes to get shiny pokemon? 
This is a learning project, I made this to explore a few libraries as I like to learn by implementing. I'd suggest you to use gameshark codes to get shinies as it saves a lot of time and trouble. 

#### Q: What emulator are you using? 
DeSmuME

#### Q: Can this code run for Pokemon games other than Diamond/Pearl/Platinum?
Yes, you have to make slight modifications for different games though. It works fine for GBA and DS emulators, I haven't tried for 3DS or Switch emulators.

#### Q: Can this be used in today's games like Sword and Shield in a legit Nintendo Switch?
No. This version is specifically designed for DS emulators.






