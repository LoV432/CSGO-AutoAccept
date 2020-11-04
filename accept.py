from PIL import ImageGrab, Image
import time
import pyautogui
from screeninfo import get_monitors


match = 10

# 320-340 is what you get when u do r+g+b of accept button. Its dumb but it works (for now)
while match < 320 or match > 340:

    # Add Delay
    time.sleep(5)

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
        x2 = round(width/100*51)
        y1 = round(height/100*56)
        y2 = round(height/100*57)
        click_x = round(width/100*50)
        click_y = round(height/100*56.64)

        # Take SS
        im = ImageGrab.grab(bbox=(x1, y1, x2, y2)) 

        # Get SS size
        width, height = im.size

        # Find center of SS
        width = round(width/2)
        height =round(height/2)


        # Find RGB values of center pixels of the SS
        rgb = im.convert('RGB') 
        r, g, b = rgb.getpixel((1, 1))
        match = r+g+b

print("matched")

# Click accept
pyautogui.click(click_x, click_y) 

print("clicked")