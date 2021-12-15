from pytz import HOUR, timezone
from datetime import datetime
import time

while(True):
    date2 = datetime.now()
    tz2 = timezone("Etc/GMT+7")
    date2 = date2.replace(tzinfo=tz2)
    time.sleep(1)
    print(date2)

    # if datetime.now().hour
