from Actions.action import Action
from keyboard_handler import KeyboardHandler

class PressKeyAction(Action):
    def __init__(self, key: str):
        self.keyboard_handler = KeyboardHandler()
        self.key = key

    def execute(self):
        self.keyboard_handler.press_key(self.key)
        return True  # Always return True since pressing a key will not fail
