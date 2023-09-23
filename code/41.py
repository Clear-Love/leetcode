'''
Author: lmio 2091319361@qq.com
Date: 2023-09-07 08:12:38
LastEditors: lmio 2091319361@qq.com
Description: 41. 缺失的第一个正数
'''

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pos = 0
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i]-1] != nums[i]:
                v = nums[i]
                nums[v-1], nums[i] = v, nums[v-1]
        while pos < n and nums[pos] == pos+1:
            pos += 1
        return pos+1