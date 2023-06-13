from pynput.mouse import Button, Controller

class ManualScroll:
    def __init__(self):
        self.mouse = Controller()

    def scroll(self, y_scroll):
        print("scrolling")

        for i in range(y_scroll):
            self.mouse.scroll(0, -1)  # Scroll down
