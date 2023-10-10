'''
Author: lmio 2091319361@qq.com
Date: 2023-10-01 11:38:28
LastEditors: lmio 2091319361@qq.com
Description: 100075. 有向图访问计数
'''

from functools import cache
from typing import List


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        answer = [0]*n
        vis = set()
        @cache
        def dfs(i: int) ->int:
            res = 1
            vis.add(i)
            if edges[i] not in vis:
                res += dfs(edges[i])
            answer[i] = res
            return res
        for i in range(n):
            if answer[i] != 0:
                continue
            dfs(i)
            vis = set()
        return answer