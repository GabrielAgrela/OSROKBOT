from Actions.action import Action
from window_handler import WindowHandler

class ScreenshotAction(Action):
    def __init__(self, x_begin, x_end, y_begin, y_end, output_path, skip_check_first_time=False):
        super().__init__(skip_check_first_time)
        self.x_begin = x_begin
        self.x_end = x_end
        self.y_begin = y_begin
        self.y_end = y_end
        self.output_path = output_path
        self.window_title = "Rise of Kingdoms"
        self.window_handler = WindowHandler()

    def execute(self):
        screenshot, win = self.window_handler.screenshot_window(self.window_title)
        
        # Crop screenshot
        width, height = screenshot.size
        left = width * self.x_begin / 100
        upper = height * self.y_begin / 100
        right = width * self.x_end / 100
        lower = height * self.y_end / 100
        
        cropped_screenshot = screenshot.crop((left, upper, right, lower))

        cropped_screenshot.save(self.output_path)
        return True
