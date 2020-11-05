from PIL import ImageGrab, Image
import time
import pyautogui
from screeninfo import get_monitors

while True:

    # 320-340 and 380-400 is what you get when u do r+g+b of accept button. Its dumb but it works (for now)
    match = 10
    while match not in range(319,341) and match not in range(379,400):

        # Add Delay
        time.sleep(2)

        # Get active window 
        # (Used try-except becuz it throws error when no window focused)
        try:
            window = pyautogui.getActiveWindow().title
        except:
            window = "NULL"

        # If active window = cs
        if window == "Counter-Strike: Global Offensive":
            
            #Get current res
            width = get_monitors()[0].width
            height = get_monitors()[0].height
            x1 = round(width/100*50)
            x2 = x1 + 1
            y1 = round(height/100*56.64)
            y2 = y1 + 1
            click_x = width
            click_y = height

            # Take SS
            im = ImageGrab.grab(bbox=(x1, y1, x2, y2))


            # Find RGB values of center pixels of the SS
            rgb = im.convert('RGB') 
            r, g, b = rgb.getpixel((0, 0))
            match = r+g+b


    # Click accept
    pyautogui.click(click_x, click_y)
    pyautogui.moveTo(0, 0)
