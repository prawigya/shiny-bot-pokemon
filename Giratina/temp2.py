from pynput.keyboard import Key, Controller
keyboard = Controller()
with keyboard.pressed(Key.cmd_r):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

keyboard.press('1')
time.sleep(1)
keyboard.release('1')
