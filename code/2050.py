'''
Author: lmio 2091319361@qq.com
Date: 2023-07-28 21:35:15
LastEditors: lmio 2091319361@qq.com
Description: 2050. 并行课程 III
'''

from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indeg = [0]*(n+1)
        begTime = [0]*(n+1)
        # 构建邻接表和入度表
        for relation in relations:
            prev_course, next_course = relation
            graph[prev_course].append(next_course)
            indeg[next_course] += 1
        q = deque()
        res = 0
        for i in range(1, n+1):
            if indeg[i] == 0:
                res = max(res, time[i-1])
                q.append(i)
        while q:
            node = q.popleft()
            start = begTime[node]
            for v in graph[node]:
                indeg[v] -= 1
                begTime[v] = max(begTime[v], start + time[node-1])
                if indeg[v] == 0:
                    res = max(res, begTime[v]+time[v-1])
                    q.append(v)
        return res 