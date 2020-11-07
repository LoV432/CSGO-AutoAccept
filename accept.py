from time import sleep
from pyautogui import pixelMatchesColor, click, moveTo, getActiveWindow, press
from screeninfo import get_monitors
import keyboard

def accept(keyboard_event):
    
    if keyboard.is_pressed("1") is True:
        print("Script Active ", end="\r")
        sleep(0.2)
        while True:
            # Add Delay

            # Get active window
            # (Used try-except becuz it throws error when no window focused)
            try:
                window = getActiveWindow().title
            except:
                window = "NULL"

            # If active window = cs
            if window == "Counter-Strike: Global Offensive":

                # Get current res and position of accept button
                x1 = round(get_monitors()[0].width / 100 * 50)
                y1 = round(get_monitors()[0].height / 100 * 56.64)

                # Take SS and compare the pixel x1,y1 with the given rgb value
                check1 = pixelMatchesColor(x1, y1, (78, 175, 82), tolerance=5)
                check2 = pixelMatchesColor(x1, y1, (93, 203, 98), tolerance=5)

                # If match found go to x1,y1 and click
                if check1 or check2 == True:
                    
                    # Click accept
                    click(x1, y1)

                    # Move mouse out of the way (Not really needed but ¯\_(ツ)_/¯)
                    moveTo(100, 200)

                if keyboard.is_pressed("1") is True:
                    print("Script Paused", end="\r")
                    sleep(0.2)
                    break

print('Press TAB to activate or pause\n')
keyboard.hook_key("1", accept)
keyboard.wait()
