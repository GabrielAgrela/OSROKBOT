
from Actions.action import Action
from pynput.mouse import  Controller

class ManualScrollAction(Action):
    def __init__(self, y_scroll=0, x_pos= 0, y_pos=0):
        self.y_scroll = y_scroll
        self.mouse = Controller()

    def execute(self):
        for i in range(self.y_scroll):
            self.mouse.scroll(0, -1)
        return True
