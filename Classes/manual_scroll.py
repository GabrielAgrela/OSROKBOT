import cv2
import numpy as np
import pyautogui

class ManualScroll:
    def __init__(self, threshold=0.65):
        self.threshold = threshold

    def scroll(self, win, y_scroll):
        print("scrolling",y_scroll)
        #click middle of the screen with pyautogui
        center_x = int(win.width // 2 + win.left)
        center_y = int(win.height // 2 + win.top)
        pyautogui.moveTo(center_x,center_y)
        for i in range(y_scroll):
            pyautogui.scroll(-1)
