import cv2
import numpy as np
import pyautogui

class ManualScroll:
    def __init__(self, threshold=0.65):
        self.threshold = threshold

    def scroll(self, win, y_scroll, x_pos, y_pos):
        print("scrolling")
        #click middle of the screen with pyautogui
        center_x = x_pos
        center_y = y_pos
        #pyautogui.moveTo(center_x,center_y)
        for i in range(y_scroll):
            pyautogui.scroll(-1)
