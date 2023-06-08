import time
from image_finder import ImageFinder
from window_handler import WindowHandler
from keyboard_handler import KeyboardHandler
import threading
from Actions.find_and_click_image_action import FindAndClickImageAction
from Actions.press_key_action import PressKeyAction
from Actions.find_image_action import FindImageAction

class GameAutomator:
    def __init__(self, window_title, image_finder, window_handler, keyboard_handler, delay=1):
        self.window_title = window_title
        self.image_finder = image_finder
        self.window_handler = window_handler
        self.keyboard_handler = keyboard_handler
        self.delay = delay
        self.stop_event = threading.Event()

    def run(self, actions_groups):
        while not self.stop_event.wait(1):  # Run every 10 seconds
            for action_group in actions_groups:
                time.sleep(2)
                for action in action_group:
                    if not action.execute():
                        break  # If action fails, stop the loop and try again after 10 seconds
                    else:
                        time.sleep(self.delay)

    def start(self, steps):
        threading.Thread(target=self.run, args=(steps,)).start()

    def stop(self):
        self.stop_event.set()

if __name__ == "__main__":
    image_finder = ImageFinder()
    window_handler = WindowHandler()
    keyboard_handler = KeyboardHandler()

    

    scout_explore = [
        FindAndClickImageAction(image_finder, 'Media/explore.png', 50, window_handler, 'Rise of Kingdoms'),
        FindAndClickImageAction(image_finder, 'Media/exploreicon.png', 0, window_handler, 'Rise of Kingdoms'),
        FindAndClickImageAction(image_finder, 'Media/exploreaction.png', 0, window_handler, 'Rise of Kingdoms'),
        FindAndClickImageAction(image_finder, 'Media/exploreaction.png', 0, window_handler, 'Rise of Kingdoms'),
        FindAndClickImageAction(image_finder, 'Media/sendaction.png', 0, window_handler, 'Rise of Kingdoms'),
        PressKeyAction(keyboard_handler, 'space')
    ]

    pick_rss = [
        FindAndClickImageAction(image_finder, 'Media/wood.png', 0, window_handler, 'Rise of Kingdoms'),
        FindAndClickImageAction(image_finder, 'Media/corn.png', 0, window_handler, 'Rise of Kingdoms'),
        FindAndClickImageAction(image_finder, 'Media/rock.png', 0, window_handler, 'Rise of Kingdoms'),
    ]

    help_alliance = [
        FindAndClickImageAction(image_finder, 'Media/alliancehelp.png', 0, window_handler, 'Rise of Kingdoms'),
    ]

    cure_troops = [
        FindAndClickImageAction(image_finder, 'Media/curetroops.png', 0, window_handler, 'Rise of Kingdoms'),
        FindAndClickImageAction(image_finder, 'Media/healaction.png', 0, window_handler, 'Rise of Kingdoms'),
    ]

    pickup_cured_troops = [
        FindAndClickImageAction(image_finder, 'Media/pickuptroopscured.png', 0, window_handler, 'Rise of Kingdoms'),
    ]

    farm_crop = [
        PressKeyAction(keyboard_handler, 'space'),
        PressKeyAction(keyboard_handler, 'f'),
        FindAndClickImageAction(image_finder, 'Media/cropland.png', 0, window_handler, 'Rise of Kingdoms'),
        FindAndClickImageAction(image_finder, 'Media/searchaction.png', 0, window_handler, 'Rise of Kingdoms'),
        FindAndClickImageAction(image_finder, 'Media/crop.png', 0, window_handler, 'Rise of Kingdoms'),
        FindAndClickImageAction(image_finder, 'Media/gatheraction.png', 0, window_handler, 'Rise of Kingdoms'),
        FindAndClickImageAction(image_finder, 'Media/newtroopaction.png', 0, window_handler, 'Rise of Kingdoms'),
        FindAndClickImageAction(image_finder, 'Media/marchaction.png', 0, window_handler, 'Rise of Kingdoms'),
        PressKeyAction(keyboard_handler, 'space'),
    ]

    actions_groups = [scout_explore,pick_rss, help_alliance, cure_troops,pickup_cured_troops]
    #actions_groups = [farm_crop]
    #actions_groups = [is_gathering]

    game_automator = GameAutomator('Rise of Kingdoms', image_finder, window_handler, keyboard_handler)
    game_automator.start(actions_groups)
