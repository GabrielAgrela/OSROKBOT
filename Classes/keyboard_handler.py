import pyautogui

class KeyboardHandler:
    def press_key(self, key):
        print("pressed ",key )
        pyautogui.press(key)
