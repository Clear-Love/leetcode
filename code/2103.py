'''
Author: lmio 2091319361@qq.com
Date: 2023-11-02 23:47:41
LastEditors: lmio 2091319361@qq.com
Description: 2103. 环和杆
'''

from collections import defaultdict


class Solution:
    def countPoints(self, rings: str) -> int:
        key = {'R':1, 'G': 1 << 1, 'B': 1 << 2}
        mark = 7
        m = defaultdict(int)
        res = set()
        n = len(rings)
        for i in range(0, n-1, 2):
            color, index = rings[i], rings[i+1]
            if index in res:
                continue
            m[index] |= key[color]
            if m[index] == mark:
                res.add(index)
        return len(res)