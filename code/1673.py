'''
Author: lmio 2091319361@qq.com
Date: 2024-05-24 16:35:27
LastEditors: lmio 2091319361@qq.com
Description: 1673. 找出最具竞争力的子序列
'''
from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)
        for i, num in enumerate(nums):
            # 单调栈 比栈顶小且剩余元素足够
            while stack and num < stack[-1] and n-i+len(stack) > k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack