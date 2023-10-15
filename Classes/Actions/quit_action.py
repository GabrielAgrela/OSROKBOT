from Actions.action import Action
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Actions.action import Action
import time

class QuitAction(Action):
    def __init__(self,OS_ROKBOT, delay=0.1,retard =0):
        self.delay = delay
        self.OS_ROKBOT = OS_ROKBOT
        self.retard = retard

    def execute(self):
        time.sleep(self.delay)
        #quit the script
        self.OS_ROKBOT.stop()
        return True
