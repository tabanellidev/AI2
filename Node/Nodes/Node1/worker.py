import pydirectinput
import pygetwindow

from threading import Thread

class Worker(Thread):
    def __init__(self, event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event = event

    def run(self) -> None:

        while True:
            w = pygetwindow.getWindowsWithTitle('METIN2')[0]
            w.activate()
            pydirectinput.press('1',1)
            pydirectinput.press('z',4)
            w1 = pygetwindow.getWindowsWithTitle('METIN2')[1]
            w1.activate()
            pydirectinput.press('1',1)
            pydirectinput.press('z',4)

            if self.event.is_set():
                print('Workers Terminated.')
                break