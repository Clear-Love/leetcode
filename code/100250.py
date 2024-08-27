'''
Author: lmio 2091319361@qq.com
Date: 2024-03-30 23:10:15
LastEditors: lmio 2091319361@qq.com
Description: 100250. 得到更多分数的最少关卡数目
'''

from itertools import accumulate
from typing import List


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        preSum = list(accumulate([1 if x else -1 for x in possible]))
        for i in range(len(possible)-1):
            if preSum[i] > preSum[-1]-preSum[i]:
                return i+1
        return -1