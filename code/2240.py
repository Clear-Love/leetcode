'''
Author: lmio 2091319361@qq.com
Date: 2023-09-01 12:55:26
LastEditors: lmio 2091319361@qq.com
Description: 2240. 买钢笔和铅笔的方案数
'''

class Solution:
    def waysToBuyPensPencils(self, total, cost1, cost2):
        n = total // cost1 + 1
        return n + floorSum(n, cost2, -cost1, total)

# 返回 sum(floor((a*i+b)/m)), i 从 0 到 n-1
def floorSum(n, m, a, b):
    res = 0
    if a < 0:
        a2 = a % m + m
        res -= n * (n - 1) // 2 * ((a2 - a) // m)
        a = a2
    if b < 0:
        b2 = b % m + m
        res -= n * ((b2 - b) // m)
        b = b2
    while True:
        if a >= m:
            res += n * (n - 1) // 2 * (a // m)
            a %= m
        if b >= m:
            res += n * (b // m)
            b %= m
        yMax = a * n + b
        if yMax < m:
            break
        n = yMax // m
        b = yMax % m
        m, a = a, m
    return res