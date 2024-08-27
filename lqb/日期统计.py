'''
Author: lmio 2091319361@qq.com
Date: 2024-04-08 19:43:52
LastEditors: lmio 2091319361@qq.com
Description: 日期统计
'''

from datetime import date


yy, mm,dd = list(map(int, input().split('/')))

dates = set()

def DAY(y: int, m: int, d: int):
    y = (2000+y) if y < 60 else (1900+y)
    try:
        day = date(y, m, d)
        dates.add(day)
    except Exception as e:
        print(e)

DAY(yy, mm, dd)
DAY(dd, yy, mm)
DAY(dd, mm, yy)

res = list(dates)

res.sort()
for d in res:
    print(d)