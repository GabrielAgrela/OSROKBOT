import cv2
import numpy as np
import pyautogui

class ManualClick:
    def __init__(self, threshold=0.65):
        self.threshold = threshold

    def click(self, win):
        #click middle of the screen with pyautogui
        center_x = int(win.width // 2 + win.left)
        center_y = int(win.height // 2 + win.top)
        pyautogui.click(center_x, center_y)
