'''
Author: lmio 2091319361@qq.com
Date: 2024-04-12 21:12:41
LastEditors: lmio 2091319361@qq.com
Description: 成绩统计
'''


n = int(input())
x, y = 0, 0
for _ in range(n):
    v = int(input())
    if v >= 60:
        x += 1
    if v >= 85:
        y += 1
print(f"{int((x*100)/n+0.5)}%")
print(f"{int((y*100)/n+0.5)}%")