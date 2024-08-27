'''
Author: lmio 2091319361@qq.com
Date: 2024-05-15 15:14:57
LastEditors: lmio 2091319361@qq.com
Description: 2523. 范围内最接近的两个质数
'''

import bisect
from math import inf
from typing import List
# 埃氏筛
# MX = 10**6

# prime = []
# is_prime = [True]*MX
# for i in range(2, MX):
#     if is_prime[i]:
#         prime.append(i)
#         # 移除所有 i 的倍数
#         for j in range(i*i, MX, i):
#             is_prime[j] = False

# 线性筛（欧拉筛）
MX = 10**6

prime = []
is_prime = [True]*(MX+1)
for i in range(2, MX+1):
    if is_prime[i]:
        prime.append(i)
    for num in prime:
        if i*num > MX:
            break
        is_prime[i*num] = False
        if i%num == 0: # 第一个质因数停止
            break

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        n = len(prime)
        i = bisect.bisect_left(prime, left) # 找到第一个大于等于 left 的质数
        if i == n:
            return [-1, -1]
        if prime[i] > right:
            return [-1, -1]
        p, q = -1, -1
        while i < n-1 and prime[i+1] <= right:
            if p < 0 or prime[i+1] - prime[i] < q - p:
                p, q = prime[i], prime[i+1]
            i += 1
        return [p, q]