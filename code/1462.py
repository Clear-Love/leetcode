'''
Author: lmio 2091319361@qq.com
Date: 2023-09-12 14:19:17
LastEditors: lmio 2091319361@qq.com
Description: 1462. 课程表 IV
'''

from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        indgree = [0] * numCourses
        isPre = [[False] * numCourses for _ in range(numCourses)]
        for p in prerequisites:
            indgree[p[1]] += 1
            graph[p[0]].append(p[1])

        queue = []
        for i in range(numCourses):
            if indgree[i] == 0:
                queue.append(i)
        while queue:
            cur = queue[0]
            queue.pop(0)
            for next in graph[cur]:
                isPre[cur][next] = True
                for i in range(numCourses):
                    isPre[i][next] = isPre[i][next] or isPre[i][cur]
                indgree[next] -= 1
                if indgree[next] == 0:
                    queue.append(next)
        res = []
        for query in queries:
            res.append(isPre[query[0]][query[1]])
        return res