'''
Author: lmio 2091319361@qq.com
Date: 2023-09-11 20:13:19
LastEditors: lmio 2091319361@qq.com
Description: 630. 课程表 III
'''

import heapq
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        q = []
        # 优先队列中所有课程的总时间
        total = 0
        for ti, di in courses:
            if total + ti <= di:
                total += ti
                heapq.heappush(q, -ti)
            elif q and -q[0] > ti:
                total -= -q[0] - ti
                heapq.heapreplace(q, -ti)
        return len(q)