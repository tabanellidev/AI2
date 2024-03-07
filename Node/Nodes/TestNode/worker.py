import pydirectinput
import pygetwindow
import time
from pygetwindow import PyGetWindowException

from threading import Thread

class Worker(Thread):
    def __init__(self, event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event = event

    def run(self) -> None:

        while True:
            time.sleep(2)
            pydirectinput.press('1',1)
            pydirectinput.press('z',4)
            time.sleep(2)
            pydirectinput.press('1',1)
            pydirectinput.press('z',4)

            if self.event.is_set():
                print('Workers Terminated.')
                break