import keyboard
from Actions.action import Action

class WaitForKeyPressAction(Action):
    def __init__(self, key,msg, skip_check_first_time=False):
        super().__init__(skip_check_first_time)
        self.key = key
        self.msg = msg

    def execute(self):
        print(f'\nPress {self.key} to {self.msg}\n')
        keyboard.wait(self.key)
        return True
