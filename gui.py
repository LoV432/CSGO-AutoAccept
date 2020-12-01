import tkinter as tkin
import tkinter.font as font
from pyautogui import pixelMatchesColor, click, moveTo, getActiveWindow
from screeninfo import get_monitors
from guiLoop import guiLoop
import winsound
x = True

#Func used to compare pixel colors with given RGB value
def check_color(c1,c2,c3):
    return pixelMatchesColor(x1, y1, (c1, c2, c3), tolerance=5)

@guiLoop
def script():
    global x1,y1
    while x == True:

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

            # Compare RGB values and if one of them true:
            if check_color(78, 175, 82) + check_color(93, 203, 98) == 1:
                
                # Click accept
                click(x1, y1)

                # Move mouse out of the way (Not really needed but ¯\_(ツ)_/¯)
                moveTo(100, 200)

        #Add delay
        yield 3


#---GUI---

#Func to start script and change button to stop
def start():
    global x
    button["text"] = "Stop"
    button["bg"] = "#4caf50"
    button["command"] = stop
    winsound.Beep(400, 100)
    x = True
    script(screen)

#Func to stop script and change button to start
def stop():
    global x
    button["text"] = "Start"
    button["bg"] = "#7f0909"
    button["command"] = start
    winsound.Beep(300, 100)
    x = False


# Basic GUI config
screen = tkin.Tk()
w = round(get_monitors()[0].width / 100 * 35)
h = round(get_monitors()[0].height / 100 * 35)
screen.geometry("500x200+"+ str(w) + "+" + str(h))
screen.title("CSGO Auto Accept")
font = font.Font(size=50)
button = tkin.Button(screen, text="Stop", font=font, width=30, height=10, bg="#4caf50", activebackground='grey', command=stop)
button.pack()
winsound.Beep(400, 100)
script(screen)
screen.mainloop()
