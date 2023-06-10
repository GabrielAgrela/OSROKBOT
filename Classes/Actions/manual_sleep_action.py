import time
from Actions.action import Action

class ManualSleepAction(Action):
    def __init__(self, break_action=False, delay=1):
        super().__init__(break_action)
        self.break_action = break_action
        self.delay = delay



    def execute(self):
        time.sleep(self.delay)
        return not self.break_action
