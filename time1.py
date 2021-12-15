from pytz import HOUR, timezone
from datetime import date, datetime
import time

while(True):
    date2 = datetime.now()
    tz2 = timezone("Etc/GMT+7")
    date2 = date2.replace(tzinfo=tz2)
    time.sleep(1)
    print(date2)

    imgname = [ "cam1_"+str(date2)+".jpg",
                "cam2_"+str(date2)+".jpg",
                "cam3_"+str(date2)+".jpg",
                "cam4_"+str(date2)+".jpg"]   

    with open('queue.txt', 'w') as f:
        for x in range(4):
            f.write(imgname[x])
            f.write('\n')
            