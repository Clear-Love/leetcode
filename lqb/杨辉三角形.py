'''
Author: lmio 2091319361@qq.com
Date: 2024-04-01 23:35:25
LastEditors: lmio 2091319361@qq.com
Description: 杨辉三角形
'''

import math


def check(k: int, n: int) ->bool:
    if n < math.comb(2*k, k):
        return False
    left, right = 2*k, n
    while left < right:
        mid = (left + right) >> 1
        v = math.comb(mid, k)
        if v >= n:
            right = mid
        else:
            left = mid+1
    if math.comb(left, k) == n:
        print((left*(left+1))//2+k+1)
        return True
    return False

n = int(input())

for i in range(16, -1, -1):
    if check(i, n):
        break