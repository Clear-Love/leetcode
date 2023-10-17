'''
Author: lmio 2091319361@qq.com
Date: 2023-10-13 15:40:14
LastEditors: lmio 2091319361@qq.com
Description: 1488. 避免洪水泛滥
'''

import bisect
from collections import deque
from typing import List

from sortedcontainers import SortedList


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        whenNotRain = SortedList()
        Rain = {}
        res = [1] * len(rains)
        for i, w in enumerate(rains):
            # 没有下雨
            if not rains[i]:
                whenNotRain.add(i)
                continue
            res[i] = -1
            if w in Rain:
                lastRainDay = Rain[w]
                if not whenNotRain or whenNotRain[-1] < lastRainDay:
                    return []
                res[whenNotRain.pop(whenNotRain.bisect_right(lastRainDay))] = w
            Rain[w] = i
        return res