import time
from pynput.keyboard import Key, Controller
from pynput import mouse
from pywinauto import Desktop

delay = 5
wait = 3
duration = 60
targetN = -1
target = "Minecraft "
t = Controller()
m = mouse.Controller()

def pressKey(controller, key):
    controller.press(key)
    time.sleep(wait)

def tapKey(controller, key):
    controller.tap(key)
    time.sleep(wait/20)

def releaseKey(controller, key):
    controller.release(key)
    time.sleep(wait)

def clickButton(controller, button):
    controller.click(button)
    time.sleep(wait)
'''
windows = Desktop(backend="uia").windows()  # creates a list of windows (and 4 other things)

for w in range(len(windows)):
    text = windows[w].window_text()
    #print(windows[w])
    #for i in range(len(text)-len(target)):
    if text[0:len(target)] == target:
        targetN = w
        print("yes, w blev:",w)
windows[target].activate
time.sleep(120)

# Minecraft 1.19.2 - Multiplayer (LAN)'''
time.sleep(delay)
for i in range(int(duration/wait)):
    clickButton(m, mouse.Button.left)
tapKey(t, Key.enter)
tapKey(t, 'd')
tapKey(t, 'o')
tapKey(t, 'n')
tapKey(t, 'e')
tapKey(t, Key.enter) 
