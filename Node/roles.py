import pydirectinput

class Role:

    name = ""

    def __init__(self, name):
        self.name = name


class Farmer(Role):
    def act(self):
        pydirectinput.press('1',1)
        pydirectinput.press('z',4)