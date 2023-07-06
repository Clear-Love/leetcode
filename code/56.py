'''
Author: lmio 2091319361@qq.com
Date: 2023-07-06 22:05:54
LastEditors: lmio 2091319361@qq.com
Description: 56. 合并区间
'''

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    res = []
    i = 0
    while i < len(intervals):
        j = i + 1
        r = intervals[i][1]
        while j < len(intervals) and intervals[j][0] <= r:
            r = max(r, intervals[j][1])
            j += 1
        res.append([intervals[i][0], r])
        i = j
    return res