import time
import threading
from action_sets import ActionSets
import keyboard
import pygetwindow as gw
class GameAutomator:
    def __init__(self, window_title, delay=0):
        self.window_title = window_title
        self.delay = delay
        self.stop_event = threading.Event()
        self.pause_event = threading.Event()

    def run(self, state_machines):
        while not self.stop_event.wait(0):  # Run every 10 seconds
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

    actions_groups = [action_sets.farm_rss()] 

    game_automator = GameAutomator('Rise of Kingdoms')
    game_automator.start(actions_groups) 
