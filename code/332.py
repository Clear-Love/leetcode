'''
Author: lmio 2091319361@qq.com
Date: 2024-05-27 19:08:28
LastEditors: lmio 2091319361@qq.com
Description: 332. 重新安排行程
'''

from collections import defaultdict, deque
import heapq
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        for u, v in tickets:
            g[u].append(v)
        for k in g.keys():
            heapq.heapify(g[k])
        stack = []
        def dfs(curr: str):
            while g[curr]:
                dfs(heapq.heappop(g[curr]))
            stack.append(curr)
        dfs("JFK")
        return stack[::-1]