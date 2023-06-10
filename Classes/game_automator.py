import time
from image_finder import ImageFinder
from window_handler import WindowHandler
from keyboard_handler import KeyboardHandler
from manual_click import ManualClick
import threading
from Actions.find_and_click_image_action import FindAndClickImageAction
from Actions.soft_find_and_click_image_action import SoftFindAndClickImageAction
from Actions.press_key_action import PressKeyAction
from Actions.find_image_action import FindImageAction
from Actions.manual_click_action import ManualClickAction
from Actions.manual_scroll_action import ManualScrollAction
from Actions.conditional_action import ConditionalAction
from Actions.manual_sleep_action import ManualSleepAction
import keyboard

class GameAutomator:
    def __init__(self, window_title, delay=1):
        self.window_title = window_title
        self.image_finder = image_finder
        self.window_handler = window_handler
        self.keyboard_handler = keyboard_handler
        self.delay = delay
        self.stop_event = threading.Event()
        self.pause_event = threading.Event()

    def run(self, actions_groups):
        while not self.stop_event.wait(1):  # Run every 10 seconds
            if self.pause_event.is_set():
                continue
            for action_group in actions_groups:
                for action in action_group:
                    if not action.execute():
                        break  # If action fails, stop the loop and try again after 10 seconds
                    else:
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
    image_finder = ImageFinder()
    window_handler = WindowHandler()
    keyboard_handler = KeyboardHandler()
    manual_click = ManualClick()

    

    scout_explore = [
        FindAndClickImageAction('Media/explore.png', offset_y=25),
        FindAndClickImageAction('Media/exploreicon.png'),
        FindAndClickImageAction('Media/exploreaction.png'),
        FindAndClickImageAction('Media/exploreaction.png'),
        FindAndClickImageAction('Media/sendaction.png'),
        PressKeyAction('space')
    ]

    pick_rss = [
        FindAndClickImageAction('Media/wood.png', check=False),
        FindAndClickImageAction('Media/corn.png', check=False),
        FindAndClickImageAction('Media/rock.png', check=False),
    ]

    help_alliance = [
        FindAndClickImageAction('Media/alliancehelp.png', offset_y=10),
    ]

    cure_troops = [
        FindAndClickImageAction('Media/curetroops.png'),
        FindAndClickImageAction('Media/healaction.png'),
    ]

    pickup_cured_troops = [
        FindAndClickImageAction('Media/pickuptroopscured.png'),
    ]

    farm_crop = [
        FindImageAction('Media/isgathering.png',check=False, dont_find=True),
        FindImageAction('Media/isreturning.png',check=False, dont_find=True),
        FindImageAction('Media/isgoing.png',check=False, dont_find=True),
        PressKeyAction('space'),
        PressKeyAction('f'),
        FindAndClickImageAction('Media/cropland.png'),
        FindAndClickImageAction('Media/searchaction.png'),
        ManualClickAction(),
        FindAndClickImageAction('Media/gatheraction.png'),
        FindAndClickImageAction('Media/newtroopaction.png'),
        FindAndClickImageAction('Media/marchaction.png'),
        PressKeyAction('space'), 
    ] 

    farm_wood = [
        FindImageAction('Media/isgathering.png', dont_find=True),
        FindImageAction('Media/isreturning.png', dont_find=True),
        FindImageAction('Media/isgoing.png', dont_find=True),
        PressKeyAction('space'),
        PressKeyAction('f'),
        FindAndClickImageAction('Media/woodland.png'),
        FindAndClickImageAction('Media/searchaction.png'),
        ManualClickAction(),
        FindAndClickImageAction('Media/gatheraction.png'),
        FindAndClickImageAction('Media/newtroopaction.png'),
        FindAndClickImageAction('Media/marchaction.png'),
        PressKeyAction('space'), 
    ] 

    farm_barb = [
        FindImageAction('Media/victory.png', skip_check_first_time=True),
        #SoftFindAndClickImageAction('Media/curetroops.png'),
        #SoftFindAndClickImageAction('Media/healaction.png'),
        FindAndClickImageAction('Media/pickuptroopscured.png', skip_check_first_time=True),
        PressKeyAction('space'),
        PressKeyAction('f'),
        FindAndClickImageAction('Media/barbland.png'),
        FindAndClickImageAction('Media/searchaction.png'),
        FindAndClickImageAction('Media/arrow.png', 40),
        FindAndClickImageAction('Media/attackaction.png'),
        FindAndClickImageAction('Media/newtroopaction.png'),
        FindAndClickImageAction('Media/marchaction.png'),
        PressKeyAction('space'),
    ]

    train_inf = [
        FindAndClickImageAction('Media/infantryhouse.png'),
        FindAndClickImageAction('Media/traininfantry.png'),
        FindAndClickImageAction('Media/t1.png'),
        FindAndClickImageAction('Media/upgrade.png'),
        FindAndClickImageAction('Media/upgradeaction.png'),
        FindAndClickImageAction('Media/infantryhouse.png'),
        FindAndClickImageAction('Media/traininfantry.png'),
        FindAndClickImageAction('Media/speedupaction.png'),
        FindAndClickImageAction('Media/useaction.png'),
        FindAndClickImageAction('Media/spam.png'),
        FindAndClickImageAction('Media/useaction.png'),
        FindAndClickImageAction('Media/infantryhouse.png'),
    ]

    reconnect = [
        FindAndClickImageAction('Media/confirm.png'),
    ]

    explore_villages = [
    PressKeyAction('z'),
    FindAndClickImageAction('Media/explorationreport.png', check=False),
    ConditionalAction(
        primary_actions=[
            FindAndClickImageAction('Media/barbreport.png', offset_x=370),
            FindAndClickImageAction('Media/villagereport.png', offset_x=370),
            
        ],
        primary_subsequent_actions=[
            ManualClickAction(),
        ],
        alternative_subsequent_actions=[
            ManualScrollAction(15)
        ],
        retry_times=5  # retry up to 5 times
    ),
        # other actions...
    ]



    #actions_groups = [scout_explore,pick_rss, help_alliance, cure_troops,pickup_cured_troops]
    actions_groups = [explore_villages]
    #actions_groups = [train_inf] 

    game_automator = GameAutomator('Rise of Kingdoms')
    game_automator.start(actions_groups)
