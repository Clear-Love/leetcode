'''
Author: lmio 2091319361@qq.com
Date: 2023-09-20 14:51:37
LastEditors: lmio 2091319361@qq.com
Description: 1552. 两球之间的磁力
'''

from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def fn(d: int) -> int:
            cnt = 1
            pre = position[0]
            for pos in position:
                if pos-pre >= d:
                    cnt += 1
                    pre = pos
            return cnt
        l, r = 0, (position[-1] - position[0])//(m-1) + 1
        while l < r:
            mid = (l+r+1) >> 1
            if fn(mid) < m:
                r = mid-1
            else:
                l = mid
        return l