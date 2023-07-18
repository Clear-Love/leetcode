'''
Author: lmio 2091319361@qq.com
Date: 2023-07-16 23:03:52
LastEditors: lmio 2091319361@qq.com
Description: 
'''
from collections import deque
from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        queue = deque()
        for r in range(len(nums)):
            while queue and queue[0] + k < nums[r] - k:
                queue.popleft()
            queue.append(nums[r])
            res = max(res, len(queue))
        return res