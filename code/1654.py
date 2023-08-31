'''
Author: lmio 2091319361@qq.com
Date: 2023-08-30 16:52:31
LastEditors: lmio 2091319361@qq.com
Description: 1654. 到家的最少跳跃次数
'''

from collections import deque
from typing import List



class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        lower,upper = 0, max(x,max(forbidden)+a+b)
        visit = set(forbidden)
        q = deque([(0,0)])
        while q:
            pos, step = q.popleft()
            if pos == x:
                return step
            if pos in visit:
                continue
            visit.add(pos)
            for diff in (a,-b):
                step += 1
                pos += diff
                if pos in visit:
                    break
                if lower <= pos <= upper:
                    q.append((pos, step))
        return -1