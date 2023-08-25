from Actions.action import Action
from image_finder import ImageFinder
from window_handler import WindowHandler
import time

class FindImageAction(Action):
    def __init__(self, image: str, count: int = 1, delay=0.1, retard=0):
        self.image_finder = ImageFinder()
        self.image = image
        self.window_handler = WindowHandler()
        self.window_title = 'Rise of Kingdoms'
        self.delay = delay
        self.retard = retard
        self.count = count  # Number of times the image must be found

    def execute(self):
        screenshot, win = self.window_handler.screenshot_window(self.window_title)
        scaling_factor, matches, num_matches, _, _, _ = self.image_finder._match_image(self.image, screenshot)

        # Check if the number of matches is greater or equal to the specified count
        if num_matches >= self.count:
            print(f"Found {self.image} {num_matches} times, satisfying the count condition of {self.count}.", "green")
            return True
        else:
            print(f"Found {self.image} {num_matches} times, not satisfying the count condition of {self.count}.", "red")
            return False
