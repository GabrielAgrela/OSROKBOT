from Actions.action import Action
from image_finder import ImageFinder
from window_handler import WindowHandler
import time
class FindAndClickImageAction(Action):
    def __init__(self, image: str,offset_x= 0, offset_y= 0, skip_check_first_time=False, check=True, dont_find=False, delay=0.5, retard=0, max_matches=0 ):
        super().__init__(skip_check_first_time)
        self.delay = delay * self.performance_multiplier
        self.image_finder = ImageFinder()
        self.image = image
        self.max_matches = max_matches
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.window_handler = WindowHandler()
        self.window_title = 'Rise of Kingdoms'
        self.check = check 
        self.retard = retard
        self.dont_find = dont_find 

    def execute(self):
        time.sleep(self.delay)
        screenshot, win = self.window_handler.screenshot_window(self.window_title)
        break_action_group = self.image_finder.find_and_click_image(self.image, screenshot, win, self.offset_x, self.offset_y, self.max_matches)
        if (break_action_group == True):
            time.sleep(self.retard)
        if not self.check:  # if check is True, no need for checks
            return True
        elif self.skip_check_first_time and self.first_run: # if its first time and theres no need to check for first time
            self.first_run = False
            break_action_group = True
        return self.dont_find != break_action_group

