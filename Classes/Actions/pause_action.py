from Actions.action import Action
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Actions.action import Action
import time

class PauseAction(Action):
    def __init__(self,game_automator, delay=0.1, retard=0):
        self.delay = delay
        self.retard =retard
        self.game_automator = game_automator

    def execute(self):
        time.sleep(self.delay)
        #quit the script
        self.game_automator.toggle_pause()
        return True
