import random
import time
class Helpers:
    @staticmethod
    def getRandomRss():
        random.seed(time.time())
        #return lambda: random.choice(["cornicon"])
        return lambda: random.choice(["cornicon","logicon"])
