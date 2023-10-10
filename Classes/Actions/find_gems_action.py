from Actions.action import Action
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Actions.action import Action
from window_handler import WindowHandler
from Actions.find_and_click_image_action import FindAndClickImageAction
import pyautogui 
import time
import numpy as np

import cv2

class FindGemAction(Action):
    def __init__(self, delay=0.1, retard=0):
        self.delay = delay
        self.retard =retard

    def execute(self):
        sleeptime=0.4
        found=0
        time.sleep(self.delay)
        WindowHandler().activate_window()
        for duration in range(1, 40):  # Loop for 1 to 5 seconds
            if duration % 4 == 1:  # Arrow left
                key = 'left'
                sleeptime=.7
            elif duration % 4 == 2:  # Arrow down
                key = 'down'
                sleeptime=0.5
            elif duration % 4 == 3:  # Arrow right
                key = 'right'
                sleeptime=.7
            else:  # Arrow up
                key = 'up'
                sleeptime=0.5
            
            
            # Simulate pressing the arrow key for 'duration' seconds
            for x in range(1, duration+1):
                #pyautogui.keyDown(key)
                time.sleep(sleeptime)
                #pyautogui.keyUp(key)
                if (FindAndClickImageAction('Media/gemdepo.png').perform() or FindAndClickImageAction('Media/gemdepo1.png').perform() or FindAndClickImageAction('Media/gemdepo2.png').perform()):
                    found+=1
                    print("found ", found)
            
            print(duration)
            
