'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 12:31:11
LastEditors: lmio 2091319361@qq.com
Description: 面试题 04.01. 节点间通路
'''

from typing import List


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        table = [[] for _ in range(n)]
        for i, j in graph:
            table[i].append(j)
        visited = set()
        res = False
        def dfs(node: int):
            nonlocal res
            if node == target:
                res = True
                return
            visited.add(node)
            for n in table[node]:
                if n not in visited:
                    dfs(n)
            visited.remove(node)
        dfs(start)
        return res