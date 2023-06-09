from abc import ABC, abstractmethod

class Action(ABC):
    def __init__(self, skip_first_time=False):
        self.skip_first_time = skip_first_time
        self.first_run = True

    @abstractmethod
    def execute(self):
        pass
