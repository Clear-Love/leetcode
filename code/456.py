'''
Author: lmio 2091319361@qq.com
Date: 2023-10-26 21:06:16
LastEditors: lmio 2091319361@qq.com
Description: 456. 132 模式
'''

from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        stack = []
        pre = [-1]*n
        min_val = []
        mn = nums[0]
        for i, num in enumerate(nums):
            mn = min(mn, num)
            min_val.append(mn)
            while stack and nums[stack[-1]] <= num:
                stack.pop()
            pre[i] = stack[-1] if stack else -1
            stack.append(i)
        for i in range(2, n):
            idx = pre[i]
            if idx != -1 and idx > 0:
                left = min_val[idx-1]
                if nums[i] > left:
                    return True
        return False