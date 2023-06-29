import time
from image_finder import ImageFinder
from window_handler import WindowHandler
from keyboard_handler import KeyboardHandler
from manual_click import ManualClick
from email_handler import EmailHandler
import threading
from Actions.find_and_click_image_action import FindAndClickImageAction
from Actions.soft_find_and_click_image_action import SoftFindAndClickImageAction
from Actions.press_key_action import PressKeyAction
from Actions.find_image_action import FindImageAction
from Actions.manual_click_action import ManualClickAction
from Actions.manual_scroll_action import ManualScrollAction
from Actions.conditional_action import ConditionalAction
from Actions.manual_sleep_action import ManualSleepAction
from Actions.email_action import EmailAction
from Actions.extract_text_action import ExtractTextAction
from Actions.screenshot_action import ScreenshotAction
from Actions.chatgpt_action import ChatGPTAction
from action_sets import ActionSets
import keyboard

class GameAutomator:
    def __init__(self, window_title, delay=0):
        self.window_title = window_title
        self.delay = delay
        self.stop_event = threading.Event()
        self.pause_event = threading.Event()

    def run(self, state_machines):
        while not self.stop_event.wait(.5):  # Run every 10 seconds
            print("\n")
            if self.pause_event.is_set():
                continue
            for state_machine in state_machines:
                while not state_machine.execute():
                    time.sleep(self.delay)

    def start(self, steps):
        threading.Thread(target=self.run, args=(steps,)).start()
        keyboard.add_hotkey('l', self.toggle_pause)  # Set up 'esc' as a hotkey to toggle pause/resume

    def stop(self):
        self.stop_event.set()

    def toggle_pause(self):
        if self.pause_event.is_set():
            self.pause_event.clear()  # Resume
        else:
            self.pause_event.set()  # Pause

if __name__ == "__main__":
    action_sets = ActionSets()

    actions_groups = [action_sets.farm_barb()] 

    game_automator = GameAutomator('Rise of Kingdoms')
    game_automator.start(actions_groups)
