from PIL import Image
from mss import mss
import pygetwindow as gw

class WindowHandler:
    def get_window(self, title):
        windows = gw.getWindowsWithTitle(title)

        if not windows:
            print(f"No window found with title: {title}")
            return None
        return windows[0]

    def screenshot_window(self, title):
        win = self.get_window(title)
        if not win:
            return None, None

        win.activate()
        sct = mss()
        monitor = {"top": win.top, "left": win.left, "width": win.width, "height": win.height}
        img = sct.grab(monitor)
        screenshot = Image.frombytes("RGB", img.size, img.rgb, "raw")
        return screenshot, win