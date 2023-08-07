'''
Author: lmio 2091319361@qq.com
Date: 2023-08-07 15:05:58
LastEditors: lmio 2091319361@qq.com
Description: 面试题 08.03. 魔术索引
'''

from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i == nums[i]:
                return i
            elif i < nums[i]:
                i = nums[i]
            else:
                i += 1
        return -1