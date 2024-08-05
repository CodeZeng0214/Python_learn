import time
print(time.localtime())
print(time.asctime(time.localtime()))

import datetime
print(datetime.date.fromtimestamp(time.time()))#根据时间戳返回日期

print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime.utcfromtimestamp(time.time()))

