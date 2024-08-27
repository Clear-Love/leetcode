'''
Author: lmio 2091319361@qq.com
Date: 2024-03-31 11:34:36
LastEditors: lmio 2091319361@qq.com
Description: 100240. 最小化曼哈顿距离
'''

from typing import List


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        a = sorted([(x+y, i) for i, (x, y) in enumerate(points)])
        b = sorted([(x-y, i) for i, (x, y) in enumerate(points)])
        c = sorted([(-x-y, i) for i, (x, y) in enumerate(points)])
        d = sorted([(-x+y, i) for i, (x, y) in enumerate(points)])
        va, vb, vc, vd = a[-1][0]-a[0][0], b[-1][0]-b[0][0], c[-1][0]-c[0][0], d[-1][0]-d[0][0]
        max_man = max(va, vb, vc, vd)
        i, j = 0, 0
        if va == max_man:
            i, j = a[0][1], a[-1][1]
        elif vb == max_man:
            i, j = b[0][1], b[-1][1]
        elif vc == max_man:
            i, j = c[0][1], c[-1][1]
        elif vd == max_man:
            i, j = d[0][1], d[-1][1]
        def man(arr: List[List[int]], idx: int):
            left, right = 0, len(arr)-1
            while arr[left][1] == idx:
                left += 1
            while arr[right][1] == idx:
                right -= 1
            return arr[right][0]-arr[left][0]
        return min(max(man(a, i), man(b, i), man(c, i), man(d, i)), max(man(a, j), man(b, j), man(c, j), man(d, j)))
