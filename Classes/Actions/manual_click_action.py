import time
from Actions.action import Action
from manual_click import ManualClick
from window_handler import WindowHandler

class ManualClickAction(Action):
    def __init__(self, y_offset= 0):
        super().__init__(y_offset)
        self.manual_click = ManualClick()
        self.window_handler = WindowHandler()
        self.y_offset = y_offset
        self.window_title = 'Rise of Kingdoms'



    def execute(self):
        time.sleep(5)
        self.manual_click.click(self.window_handler.get_window(self.window_title),self.y_offset)
        return True
