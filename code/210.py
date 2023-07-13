'''
Author: lmio 2091319361@qq.com
Date: 2023-07-11 17:49:36
LastEditors: lmio 2091319361@qq.com
Description: 
'''
from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        res = []
        queue = deque()
        # 初始化入度表和邻接表
        for cur, node in prerequisites:
            indegrees[cur] += 1
            adjacency[node].append(cur)
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
        # 广度优先
        while queue:
            node = queue.popleft()
            res.append(node)
            for cur in adjacency[node]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0: 
                    queue.append(cur)
        if len(res) == numCourses:
            return res
        return []