'''
Author: lmio 2091319361@qq.com
Date: 2024-04-12 23:09:48
LastEditors: lmio 2091319361@qq.com
Description: 技能升级
'''

import heapq


n, m = list(map(int, input().split()))
skill = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    heapq.heappush(skill, (-a, b))
res = 0
while skill and m:
    a, b = heapq.heappop(skill)
    a = -a
    res += a
    a -= b
    if a > 0:
        heapq.heappush(skill, (-a, b))
    m -= 1

print(res)