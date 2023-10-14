import time
from Actions.action import Action
from manual_move import ManualMove
from window_handler import WindowHandler
import time
from PIL import ImageGrab
import pyautogui
from colorsys import rgb_to_hsv

class CheckColorAction(Action):
    def __init__(self,x=50,y=50, delay=0, retard=0.0):
        self.manual_move = ManualMove()
        self.window_handler = WindowHandler()
        self.delay = delay
        self.window_title = 'Rise of Kingdoms'
        self.x = x
        self.y = y
        self.retard = retard



    def execute(self):
        screenshot, win = self.window_handler.screenshot_window(self.window_title)

        x = int(screenshot.width * self.x / 100)
        y = int(screenshot.height * self.y / 100)
        screenshot.save("idk.png")
        print("x ", x, " y ", y)

        # Extract the color at the center of the screenshot
        color = screenshot.getpixel((x, y))
        

        # Convert RGB to HSV for easier color comparison
        r, g, b = color
        target_h, _, _ = rgb_to_hsv(0, 255, 0)  # HSV value of pure green
        color_h, _, _ = rgb_to_hsv(r, g, b)

        # Set a threshold for color difference (adjust as needed)
        threshold = 10.0 / 360.0  # 10 degrees in the HSV color space

        # Check if the color is close to green
        if abs(color_h - target_h) < threshold:
            print("Green: ", color)
            return True
        else:
            print("NOT GREEN ", color)
            return False
