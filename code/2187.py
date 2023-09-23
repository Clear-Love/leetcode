'''
Author: lmio 2091319361@qq.com
Date: 2023-09-18 17:07:55
LastEditors: lmio 2091319361@qq.com
Description: 2187. 完成旅途的最少时间
'''

from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 0, totalTrips*min(time)
        while l < r:
            mid = (l+r) >> 1
            if sum([mid//v for v in time]) < totalTrips:
                l = mid+1
            else:
                r = mid
        return l