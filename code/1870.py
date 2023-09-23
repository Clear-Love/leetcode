'''
Author: lmio 2091319361@qq.com
Date: 2023-09-18 22:53:45
LastEditors: lmio 2091319361@qq.com
Description: 1870. 准时到达的列车最小时速
'''

import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l, r = 1, 10**7
        n = len(dist)
        while l < r:
            mid = (l+r) >> 1
            if sum([math.ceil(dist[i]/mid) for i in range(n-1)]) + dist[-1]/mid > hour:
                l = mid+1
            else:
                r = mid
        return l if sum([math.ceil(dist[i]/l) for i in range(n-1)]) + dist[-1]/l <= hour else -1