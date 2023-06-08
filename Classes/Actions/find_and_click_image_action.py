from Actions.action import Action
from image_finder import ImageFinder
from window_handler import WindowHandler

class FindAndClickImageAction(Action):
    def __init__(self, image_finder: ImageFinder, image: str, offset: int, window_handler: WindowHandler, window_title: str):
        self.image_finder = image_finder
        self.image = image
        self.offset = offset
        self.window_handler = window_handler
        self.window_title = window_title

    def execute(self):
        screenshot, win = self.window_handler.screenshot_window(self.window_title)
        return self.image_finder.find_and_click_image(self.image, screenshot, win, self.offset)
