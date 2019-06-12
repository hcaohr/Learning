import pytz
import time
from datetime import datetime


tz = pytz.timezone('America/New_York')

d_time = datetime.strptime(str(datetime.now(tz).date()) + '18:00', '%Y-%m-%d%H:%M')
d_time1 = datetime.strptime(str(datetime.now(tz).date()) + '00:00', '%Y-%m-%d%H:%M')

a = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
print(a)

if a > d_time and a < d_time1:
    pass
    print("yes")
else:
    b = time.mktime(time.strptime(a,'%Y-%m-%d %I:%M:%S'))+int(3)*3600
    print(time.strftime("%Y-%m-%d %I:%M %p",time.localtime(b)))