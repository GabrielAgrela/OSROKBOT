import time
from Actions.action import Action
from manual_move import ManualMove
from window_handler import WindowHandler

class ManualMoveAction(Action):
    def __init__(self,x=50,y=50, delay=0, remember_position=False, retard=0.0):
        self.manual_move = ManualMove()
        self.window_handler = WindowHandler()
        self.delay = delay
        self.window_title = 'Rise of Kingdoms'
        self.x = x
        self.y = y
        self.remember_position = remember_position
        self.retard = retard



    def execute(self):
        time.sleep(self.delay)
        self.manual_move.move(self.window_handler.get_window(self.window_title),self.x,self.y, self.remember_position)
        return True
