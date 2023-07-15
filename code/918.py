'''
Author: lmio 2091319361@qq.com
Date: 2023-07-15 14:41:14
LastEditors: lmio 2091319361@qq.com
Description: 918. 环形子数组的最大和
'''
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        start = nums[0]
        maxSubArr = start
        minSubArr = start
        maxCur = start
        minCur = start
        for i in range(1, len(nums)):
            v = nums[i]
            maxCur = max(v, maxCur+v)
            minCur = min(v, minCur+v)
            maxSubArr = max(maxSubArr, maxCur)
            minSubArr = min(minSubArr, minCur)
        if maxSubArr < 0:
            return maxSubArr
        sumArr = sum(nums)
        return max(sumArr-minSubArr, maxSubArr)
        
