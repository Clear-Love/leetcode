'''
Author: lmio 2091319361@qq.com
Date: 2023-09-01 14:07:23
LastEditors: lmio 2091319361@qq.com
Description: 239. 滑动窗口最大值
'''

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        queue = deque()
        for i in range(k):
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
        res = [queue[0]]
        for i in range(k, len(nums)):
            if queue[0] == nums[i-k]:
                queue.popleft()
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
            res.append(queue[0])
        return res