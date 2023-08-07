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

        sct = mss()
        monitor = {"top": win.top, "left": win.left, "width": win.width, "height": win.height}
        try:
            img = sct.grab(monitor)
            print("apanhou o monitor")
        finally:
            print("erro ao apanhar o monitor",)
            sct.close()
        screenshot = Image.frombytes("RGB", img.size, img.rgb, "raw")
        print("tirou screenshot")
        return screenshot, win

    
    def activate_window(self, title="Rise of Kingdoms"):
        print("tentou ativar window")
        win = self.get_window(title)
        win.activate()
        print("ativou window")
        return 