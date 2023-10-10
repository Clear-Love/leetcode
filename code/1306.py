'''
Author: lmio 2091319361@qq.com
Date: 2023-10-05 20:37:33
LastEditors: lmio 2091319361@qq.com
Description: 1306. 跳跃游戏 III
'''

from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        n = len(arr)
        used = set([start])
        q = deque([start])
        while len(q) > 0:
            u = q.popleft()
            for v in [u + arr[u], u - arr[u]]:
                if 0 <= v < n and v not in used:
                    if arr[v] == 0:
                        return True
                    q.append(v)
                    used.add(v)
        return False