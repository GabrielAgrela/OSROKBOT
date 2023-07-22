import keyboard
from Actions.action import Action

class WaitForKeyPressAction(Action):
    def __init__(self, key, skip_check_first_time=False):
        super().__init__(skip_check_first_time)
        self.key = key

    def execute(self):
        print(f'Waiting for {self.key} press...')
        keyboard.wait(self.key)
        print(f'{self.key} pressed!')
        return True
