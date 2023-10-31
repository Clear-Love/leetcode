'''
Author: lmio 2091319361@qq.com
Date: 2023-10-27 16:49:02
LastEditors: lmio 2091319361@qq.com
Description: 2289. 使数组按非递减顺序排列
'''

from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        res = 0
        stack = []
        for num in nums:
            mt = 0
            while stack and stack[-1][0] <= num:
                mt = max(mt, stack.pop()[1])
            mt = mt+1 if stack else 0
            res = max(res, mt)
            stack.append(num, mt)
        return