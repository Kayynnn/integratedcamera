
from pytz import HOUR, timezone
from datetime import datetime
import time
import os

if os.path.isfile('queue.txt'):
    with open('queue.txt') as f:
        lines = f.readlines()
        for z in lines:
            print(z)
            print("woe") 
    # if datetime.now().hourasdfasf
