'''
Author: lmio 2091319361@qq.com
Date: 2024-03-19 16:18:24
LastEditors: lmio 2091319361@qq.com
Description: 1793. 好子数组的最大分数
'''

from math import inf
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        stack = []
        nums.append(-inf)
        res = 0
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                v = nums[stack.pop()]
                l = stack[-1]+1 if stack else 0
                if l <= k <= i-1:
                    res = max(res, v*(i-l))
            stack.append(i)
        return res

print(Solution().maximumScore([1, 4,3,7,4,5], 3))