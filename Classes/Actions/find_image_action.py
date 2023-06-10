from Actions.action import Action
from image_finder import ImageFinder
from window_handler import WindowHandler

class FindImageAction(Action):
    def __init__(self, image: str, skip_check_first_time=False, check=True, dont_find=False):
        super().__init__(skip_check_first_time)
        super().__init__(check)
        super().__init__(dont_find)
        self.image_finder = ImageFinder()
        self.image = image
        self.window_handler = WindowHandler()
        self.window_title = 'Rise of Kingdoms'
        self.check = check 
        self.dont_find = dont_find 

    def execute(self):
        screenshot, win = self.window_handler.screenshot_window(self.window_title)
        break_action_group = self.image_finder.find_image(self.image, screenshot)
        if not self.check:  # if check is false, no need for checks
            return True
        elif self.skip_check_first_time and self.first_run: # if its first time and theres no need to check for first time
            self.first_run = False
            break_action_group =  True
        return self.dont_find != break_action_group
