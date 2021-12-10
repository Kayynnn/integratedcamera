from pytz import HOUR, timezone
from datetime import datetime
import time

while(True):
    date = datetime.now()
    tz = timezone("Etc/GMT+7")
    date = date.replace(tzinfo=tz)
    time.sleep(1)
    tes = str(date) # + str(date.minute)
    print(tes)

    # if datetime.now().hour
