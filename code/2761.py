'''
Author: lmio 2091319361@qq.com
Date: 2023-08-02 18:58:44
LastEditors: lmio 2091319361@qq.com
Description: 2761. 和等于目标值的质数对
'''

import math
from typing import List


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        is_prime = [True] * (n+1)
        for i in range(2, n+1):
            if is_prime[i]:
                for j in range(i*2, n+1, i):
                    is_prime[j] = False
        res = []
        for i in range(2, n//2 + 1):
            if is_prime[i] and is_prime[n-i]:
                res.append([i, n-i])
        return res
