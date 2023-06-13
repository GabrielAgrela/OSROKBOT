import cv2
import numpy as np
import pyautogui

class ManualClick:
    def __init__(self, threshold=0.65):
        self.threshold = threshold

    def click(self, win, x_percentage, y_percentage):
        # click at a specific percentage of the screen with pyautogui
        click_x = int(win.left + win.width * x_percentage / 100)
        click_y = int(win.top + win.height * y_percentage / 100)
        pyautogui.click(click_x, click_y)

