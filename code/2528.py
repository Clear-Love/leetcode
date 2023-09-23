'''
Author: lmio 2091319361@qq.com
Date: 2023-09-20 15:05:44
LastEditors: lmio 2091319361@qq.com
Description: 2528. 最大化城市的最小供电站数目
'''

from itertools import accumulate
from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        preSum = list(accumulate(stations, initial=0))
        for i in range(n):
            stations[i] = preSum[min(i+r+1, n)] - preSum[max(i-r, 0)]
        def check(min_power: int) -> bool:
            diff = [0]*n
            sumD, need = 0, 0
            for i, power in enumerate(stations):
                sumD += diff[i]
                d = min_power -(sumD+power)
                # 需要供电站
                if d > 0:
                    sumD += d
                    need += d
                    if need > k:
                        return False
                    if i+2*r+1 < n:
                        diff[i+2*r+1] -= d
            return True
        left = min(stations)
        right = left+k+1
        while left < right:
            mid = (left+right+1) >> 1
            if check(mid):
                left = mid
            else:
                right = mid-1
        return left