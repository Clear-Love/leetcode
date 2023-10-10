'''
Author: lmio 2091319361@qq.com
Date: 2023-10-03 21:25:50
LastEditors: lmio 2091319361@qq.com
Description: 802. 找到最终的安全状态
'''

from collections import defaultdict, deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        out = [0] * n
        edges = defaultdict(list)
        for i, nodes in enumerate(graph):
            for node in nodes:
                edges[node].append(i)
                out[i] += 1
        q = deque([])
        for i in range(n):
            if not out[i]:
                q.append(i)
        while q:
            node = q.popleft()
            for front in edges[node]:
                out[front] -= 1
                if not out[front]:
                    q.append(front)
        return [i for i in range(n) if not out[i]]