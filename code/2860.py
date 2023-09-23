'''
Author: lmio 2091319361@qq.com
Date: 2023-09-18 11:57:06
LastEditors: lmio 2091319361@qq.com
Description: 2860. 让所有学生保持开心的分组方法数
'''

from typing import List


class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        res = 0 if nums[0] == 0 else 1
        n = len(nums)
        for i in range(n-1):
            cnt = i+1
            v = nums[i]
            if cnt > v and cnt < nums[i+1]:
                res += 1
        return res+1 if n > nums[-1] else res