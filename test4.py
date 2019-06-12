import re
import time
from datetime import datetime, date, timedelta
import pytz


a = re.split('\D+', "03:06")
print(a)

# print(time.localtime())
#
# print(time.time())
#
# print(time.ctime(1542602881.8542247))
#
# print(time.strftime("%I:%M %p", time.localtime()))
#
# a = re.split('\D+', '12:50 pm')
# print(a)


# 范围时间
# y_time = datetime.strptime(str(datetime.now().date() + timedelta(days= -1)) + '18:00', '%Y-%m-%d%H:%M')
# print(y_time)
# y_time1 = datetime.strptime(str(datetime.now().date() + timedelta(days= -1)) + '23:59', '%Y-%m-%d%H:%M')
# print(y_time1)
y_time = datetime.strptime(str(datetime.now().date()) + '14:00', '%Y-%m-%d%H:%M')
y_time1 = datetime.strptime(str(datetime.now().date()) + '23:59', '%Y-%m-%d%H:%M')
d_time = datetime.strptime(str(datetime.now().date()) + '00:00', '%Y-%m-%d%H:%M')
d_time1 = datetime.strptime(str(datetime.now().date()) + '9:00', '%Y-%m-%d%H:%M')

# 当前时间
n_time = datetime.now()
print(n_time)

# 判断当前时间是否在范围时间内
if n_time > y_time and n_time < y_time1:
    pass
    print("yes")
else:
    n = str(n_time).split('.')
    print(n)
    a = time.strptime(n[0], '%Y-%m-%d %H:%M:%S')
    print(a)
    b = time.mktime(a)
    print(b)
    c = b + 3600 * 3
    print(c)
    print(time.ctime(b + 3600 * 3))
