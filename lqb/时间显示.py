'''
Author: lmio 2091319361@qq.com
Date: 2024-04-01 23:06:34
LastEditors: lmio 2091319361@qq.com
Description: 时间显示
'''

import datetime

import pytz

t = float(input())
print(t)
print(datetime.datetime.fromtimestamp(t//1000, tz=pytz.timezone("UTC")).strftime("%H:%M:%S"))
