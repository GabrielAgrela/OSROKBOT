from Actions.action import Action
from keyboard_handler import KeyboardHandler
from window_handler import WindowHandler
import time

class PressKeyAction(Action):
    def __init__(self, key: str, delay=0, retard=0):
        self.keyboard_handler = KeyboardHandler()
        self.key = key
        self.delay = delay
        self.retard = retard
        self.window_handler = WindowHandler()

    def execute(self):
        time.sleep(self.delay)
        self.window_handler.activate_window()
        self.keyboard_handler.press_key(self.key)
        return True  # Always return True since pressing a key will not fail
