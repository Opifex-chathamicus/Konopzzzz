import gitwrapper
import random
import time
import json


class Konops:

    def __init__(self):
        #configuration path
        self.cpath="config/"
        #module path
        self.mpath="modules/"
        #data path
        self.dpath="data/"

    def sleep(self):
        sleep_time = random.randint(120, 1000)
        time.sleep(sleep_time)