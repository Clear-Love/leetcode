'''
Author: lmio 2091319361@qq.com
Date: 2023-07-06 22:27:00
LastEditors: lmio 2091319361@qq.com
Description: 57.插入区间
'''

from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if len(intervals) == 0:
        return [newInterval]
    left, right = newInterval[0], newInterval[1]
    res = []
    for i, v in enumerate(intervals):
        l, r = v[0], v[1]
        if l > right:
            res.append([left, right])
            return res + intervals[i:]
        elif r < left:
            res.append([l, r])
        else:
            left, right = min(l, left), max(r, right)
    res.append([left, right])
    return res