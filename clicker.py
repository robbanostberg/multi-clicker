import time
from pynput.keyboard import Key, Controller
from pynput.mouse import Controller, Button
from pywinauto import Desktop

wait = 1

def pressKey(controller, key):
    controller.press(key)
    time.sleep(wait)

def tapKey(controller, key):
    controller.tap(key)
    time.sleep(wait)

def releaseKey(controller, key):
    controller.release(key)
    time.sleep(wait)

windows = Desktop(backend="uia").windows()  # creates a list of windows (and 4 other things)
for w in windows:
    print(w.window_text())
time.sleep(120)