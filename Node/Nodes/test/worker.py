import pydirectinput
import pygetwindow
import time
from pygetwindow import PyGetWindowException


def act():
    time.sleep(2)
    pydirectinput.press('1',1)
    pydirectinput.press('z',4)
    time.sleep(2)
    pydirectinput.press('1',1)
    pydirectinput.press('z',4)