'''
Author: lmio 2091319361@qq.com
Date: 2023-10-18 19:49:40
LastEditors: lmio 2091319361@qq.com
Description: 1203. 项目管理
'''

from collections import defaultdict, deque
from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = {}
        items = defaultdict(list)
        for i, g in enumerate(group):
            items[g].append(i)
            key = i if g == -1 else g+n
            degree[key] = 0
        deg = defaultdict(int)
        for i, before in enumerate(beforeItems):
            x = i if group[i] == -1 else group[i]+n
            for v in before:
                y = v if group[v] == -1 else group[v]+n
                # 团队内部
                if x == y:
                    graph[v].append(i)
                    deg[i] += 1
                    continue
                graph[y].append(x)
                degree[x] += 1
        q = deque(k for k, v in degree.items() if v == 0)
        def f(x) -> list:
            ans = []
            q = deque(v for v in items[x] if deg[v] == 0)
            while q:
                v = q.popleft()
                ans.append(v)
                for y in graph[v]:
                    deg[y] -= 1
                    if not deg[y]:
                        q.append(y)
            return ans
        res = []
        while q:
            x = q.popleft()
            if x < n:
                res.append(x)
            else:
                path = f(x-n)
                if len(path) != len(items[x-n]):
                    return []
                res += path
            for y in graph[x]:
                degree[y] -= 1
                if not degree[y]:
                    q.append(y)
        return res if len(res) == n else []