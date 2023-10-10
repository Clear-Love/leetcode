'''
Author: lmio 2091319361@qq.com
Date: 2023-10-03 21:14:39
LastEditors: lmio 2091319361@qq.com
Description: 1376. 通知所有员工所需的时间
'''

from collections import deque
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for i, x in enumerate(manager):
            if i == headID:
                continue
            graph[x].append(i)
        res = 0
        q = deque([(headID, 0)])
        while q:
            x, t = q.popleft()
            # 没有下属
            if not graph[x]:
                res = max(res, t)
            t += informTime[x]
            for y in graph[x]:
                q.append((y, t))
        return res