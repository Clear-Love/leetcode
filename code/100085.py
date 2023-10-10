'''
Author: lmio 2091319361@qq.com
Date: 2023-10-08 21:18:16
LastEditors: lmio 2091319361@qq.com
Description: 100085. 最小处理时间
'''

from collections import deque
from typing import List


class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        res = 0
        tasks.sort(reverse=True)
        t = deque(tasks)
        processorTime.sort()
        p = deque(processorTime)
        while t:
            time = p.popleft()
            cost = 0
            for _ in range(4):
                if not t:
                    break
                cost = max(cost, t.popleft())
            p.append(time+cost)
            res = max(time+cost, res)
        return res