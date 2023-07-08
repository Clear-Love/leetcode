'''
Author: lmio 2091319361@qq.com
Date: 2023-07-07 12:58:31
LastEditors: lmio 2091319361@qq.com
Description: 452. 用最少数量的箭引爆气球
'''

from typing import List


def findMinArrowShots(points: List[List[int]]) -> int:
    points.sort(key=lambda x: x[0])
    res = 0
    right = points[0][1]
    for v in points:
        l, r = v[0], v[1]
        if l > right:
            right = r
            res += 1
        else:
            right = min(right, r)
    return res+1