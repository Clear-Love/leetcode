'''
Author: lmio 2091319361@qq.com
Date: 2023-08-11 16:34:14
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.06. 最小差
'''

from typing import List


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        n, m = len(a), len(b)
        p1, p2 = 0, 0
        a.sort()
        b.sort()
        res = abs(a[p1] - b[p2])
        while p1 < n:
            gap = abs(a[p1] - b[p2])
            while p2+1 < m and (tmp := abs(a[p1] - b[p2+1])) < gap:
                p2 += 1
                gap = tmp
            res = min(res, gap)
            p1 += 1
        return res