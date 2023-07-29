'''
Author: lmio 2091319361@qq.com
Date: 2023-07-29 21:36:51
LastEditors: lmio 2091319361@qq.com
Description: 1466. 重新规划路线
'''
from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res=0
        d=defaultdict(list)
        dc=set([tuple(c) for c in connections])
        visited=[False]*n
        # 建立无向图
        for a,b in connections:
            d[a].append(b)
            d[b].append(a)
        def dfs(i):
            nonlocal res
            visited[i]=True
            for c in d[i]:
                if not visited[c]:
                    if (i,c) in dc:
                        res+=1
                    dfs(c)
        dfs(0)
        return res