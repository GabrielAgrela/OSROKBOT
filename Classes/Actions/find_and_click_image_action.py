from Actions.action import Action
from image_finder import ImageFinder
from window_handler import WindowHandler
import time
class FindAndClickImageAction(Action):
    def __init__(self, image: str,offset_x= 0, offset_y= 0, delay=0.2, retard=0, max_matches=0 ):
        
        self.delay = delay
        self.image_finder = ImageFinder()
        self.image = image
        self.max_matches = max_matches
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.window_handler = WindowHandler()
        self.window_title = 'Rise of Kingdoms'
        self.retard = retard

    def execute(self):
        screenshot, win = self.window_handler.screenshot_window(self.window_title)
        break_action_group = self.image_finder.find_and_click_image(self.image, screenshot, win, self.offset_x, self.offset_y, self.max_matches)
        return break_action_group

