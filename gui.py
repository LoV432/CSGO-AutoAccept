import tkinter as tkin
import tkinter.font as font
from pyautogui import pixelMatchesColor, click, moveTo, getActiveWindow
from screeninfo import get_monitors
from guiLoop import guiLoop
import winsound
s = True

#Func used to get position of the pixel and compare pixel colors with given RGB value
def check_color(c1,c2,c3,x,y):
    global x1,y1

    # Get current res and position of accept button
    x1 = round(get_monitors()[0].width / 100 * x)
    y1 = round(get_monitors()[0].height / 100 * y)

    # Compare Color and Return
    return pixelMatchesColor(x1, y1, (c1, c2, c3), tolerance=5)

@guiLoop
def script():
    while s == True:

        # Get active window
        # (Used try-except becuz it throws error when no window focused)
        try:
            window = getActiveWindow().title
        except:
            window = "NULL"

        # If active window = cs
        if window == "Counter-Strike: Global Offensive":

            # Compare RGB values and if one of them true:
            if check_color(78, 175, 82, 50, 56.64) + check_color(93, 203, 98, 50, 56.64) == 1:
                
                # Click accept
                click(x1, y1)

                # Move mouse out of the way (Not really needed but ¯\_(ツ)_/¯)
                moveTo(100, 200)

            # Stop script when in game
            elif check_color(232,232,232, 2.8125, 35.44921875) is True:

                stop()
        #Add delay
        yield 3


#---GUI---

#Func to start script and change button to stop
def start():
    global s
    button["text"] = "Stop"
    button["bg"] = "#4caf50"
    button["command"] = stop
    winsound.Beep(400, 100)
    s = True
    script(screen)

#Func to stop script and change button to start
def stop():
    global s
    button["text"] = "Start"
    button["bg"] = "#7f0909"
    button["command"] = start
    winsound.Beep(300, 100)
    s = False


# Basic GUI config
screen = tkin.Tk()
w = round(get_monitors()[0].width / 100 * 30)
h = round(get_monitors()[0].height / 100 * 30)
screen.geometry("500x200+"+ str(w) + "+" + str(h))
screen.title("CSGO Auto Accept")
font = font.Font(size=50)
button = tkin.Button(screen, text="Stop", font=font, width=30, height=10, bg="#4caf50", activebackground='grey', command=stop)
button.pack()
winsound.Beep(400, 100)
script(screen)
screen.mainloop()
