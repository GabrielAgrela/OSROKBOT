import time
from Actions.action import Action
from manual_click import ManualClick
from window_handler import WindowHandler

class ManualClickAction(Action):
    def __init__(self, window_handler: WindowHandler, manual_click: ManualClick, y_offset: int, window_title: str):
        self.manual_click = manual_click
        self.window_handler = window_handler
        self.y_offset = y_offset
        self.window_title = window_title



    def execute(self):
        time.sleep(2)
        self.manual_click.click(self.window_handler.get_window(self.window_title),self.y_offset)
        return True
