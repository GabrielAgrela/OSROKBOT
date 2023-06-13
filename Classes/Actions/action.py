from abc import ABC, abstractmethod

class Action(ABC):
    def __init__(self, skip_check_first_time: bool):
        self.skip_check_first_time = skip_check_first_time
        self.first_run = True
        self.performance_multiplier = 10

    @abstractmethod
    def execute(self):
        pass
