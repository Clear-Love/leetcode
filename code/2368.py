'''
Author: lmio 2091319361@qq.com
Date: 2024-03-13 20:40:28
LastEditors: lmio 2091319361@qq.com
Description: 2368. 受限条件下可到达节点的数目
'''

from collections import defaultdict
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        vis = set(restricted)
        def dfs(i: int):
            if i in vis:
                return
            vis.add(i)
            for j in graph[i]:
                dfs(j)
        dfs(0)
        return len(vis) - len(restricted)