import time
import threading
from action_sets import ActionSets
from signal_emitter import SignalEmitter
import keyboard
import pygetwindow as gw
from PyQt5.QtCore import pyqtSignal
class GameAutomator:
    def __init__(self, window_title, delay=0):
        
        self.window_title = window_title
        self.delay = delay
        self.stop_event = threading.Event()
        self.pause_event = threading.Event()
        self.signal_emitter = SignalEmitter()

    def run(self, state_machines):
        self.stop_event.clear() # Clear the stop event here
        
        def run_single_machine(machine):
            while not self.stop_event.is_set():
                if self.pause_event.is_set():
                    time.sleep(self.delay) # sleep a little to reduce CPU usage
                    continue
                if machine.execute():
                    time.sleep(self.delay)

        threads = [threading.Thread(target=run_single_machine, args=(machine,)) for machine in state_machines]
        for t in threads:
            t.start()

        for t in threads:
            t.join()


    def start(self, steps):
        threading.Thread(target=self.run, args=(steps,)).start()

    def stop(self):
        self.stop_event.set()

    def toggle_pause(self):
        if self.pause_event.is_set():
            self.pause_event.clear()  # Resume
        else:
            self.pause_event.set()  # Pause
        self.signal_emitter.pause_toggled.emit(self.pause_event.is_set()) # Emit the signal using the signal emitter


    def is_paused(self):
        return self.pause_event.is_set()


if __name__ == "__main__":
    

    game_automator = GameAutomator('Rise of Kingdoms')

    action_sets = ActionSets(game_automator=game_automator)

    actions_groups = [action_sets.farm_rss(), action_sets.emailtest()]

    game_automator.start(actions_groups) 
