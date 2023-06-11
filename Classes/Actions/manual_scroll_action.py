import time
from Actions.action import Action
from manual_scroll import ManualScroll
from window_handler import WindowHandler

class ManualScrollAction(Action):
    def __init__(self, y_scroll=0, x_pos= 0, y_pos=0):
        self.manual_scroll = ManualScroll()
        self.window_handler = WindowHandler()
        self.y_scroll = y_scroll
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.window_title = 'Rise of Kingdoms'



    def execute(self):
        time.sleep(2)
        self.manual_scroll.scroll(self.window_handler.get_window(self.window_title),self.y_scroll,self.x_pos,self.y_pos)
        return True
