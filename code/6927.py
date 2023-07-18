'''
Author: lmio 2091319361@qq.com
Date: 2023-07-16 21:33:58
LastEditors: lmio 2091319361@qq.com
Description: 6927. 合法分割的最小下标
'''

from collections import Counter
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        totalFreq = Counter(nums)
        curFreq = {}
        for i in range(len(nums)):
            curFreq[nums[i]] = curFreq.get(nums[i], 0) + 1
            if curFreq[nums[i]] * 2 > (i+1) and (totalFreq[nums[i]] - curFreq[nums[i]]) * 2 > (len(nums)-1-i):
                return i
        return -1