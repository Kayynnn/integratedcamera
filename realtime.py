import datetime
import time

t = datetime.datetime.utcnow()

while (True):
    print('Time = ', t)
    time.sleep(1)