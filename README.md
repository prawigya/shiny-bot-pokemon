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
