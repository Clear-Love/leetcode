'''
Author: lmio 2091319361@qq.com
Date: 2023-07-11 16:45:12
LastEditors: lmio 2091319361@qq.com
Description: 207. 课程表
'''

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
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
            numCourses -= 1
            for cur in adjacency[node]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0: 
                    queue.append(cur)
        return numCourses == 0