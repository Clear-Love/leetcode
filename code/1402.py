'''
Author: lmio 2091319361@qq.com
Date: 2023-10-22 00:32:12
LastEditors: lmio 2091319361@qq.com
Description: 1402. 做菜顺序
'''

from itertools import accumulate
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        preSum = list(accumulate(satisfaction, initial=0))
        res = 0
        for i in range(1, n+1):
            res += i*satisfaction[i-1]
        l, r = 0, n
        while (s:= preSum[r] - preSum[l]) < 0:
            res -= s
            l += 1
        return res