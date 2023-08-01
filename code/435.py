'''
Author: lmio 2091319361@qq.com
Date: 2023-07-31 20:26:14
LastEditors: lmio 2091319361@qq.com
Description: 435. 无重叠区间
'''

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        res = 0
        i = 0
        while i < n:
            r = intervals[i][1]
            i += 1
            while i < n and intervals[i][0] < r:
                i += 1
                res += 1
        return res