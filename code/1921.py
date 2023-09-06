'''
Author: lmio 2091319361@qq.com
Date: 2023-09-03 20:04:50
LastEditors: lmio 2091319361@qq.com
Description: 1921. 消灭怪物的最大数量
'''

from collections import deque
import math
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        gap = deque(sorted([math.ceil(dist[i]/speed[i]) for i in range(n)]))
        res = 0
        for i, v in enumerate(gap):
            if v <= i:
                break                
            res += 1
        return res