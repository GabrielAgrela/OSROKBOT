from abc import ABC, abstractmethod
from window_handler import WindowHandler

class Action(ABC):
    def __init__(self, skip_check_first_time: bool):
        self.skip_check_first_time = skip_check_first_time
        self.first_run = True
        self.performance_multiplier = 1

    @abstractmethod
    def execute(self):
        pass

    def perform(self):
        result = self.execute()
        #WindowHandler().activate_window("OSROKBOT")
        return result