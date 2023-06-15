from Actions.action import Action
from keyboard_handler import KeyboardHandler
import time

class PressKeyAction(Action):
    def __init__(self, key: str, delay=0, retard=0):
        self.keyboard_handler = KeyboardHandler()
        self.key = key
        self.delay = delay
        self.retard = retard

    def execute(self):
        time.sleep(self.delay)
        self.keyboard_handler.press_key(self.key)
        time.sleep(self.retard)
        return True  # Always return True since pressing a key will not fail
