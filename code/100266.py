'''
Author: lmio 2091319361@qq.com
Date: 2024-03-31 11:02:31
LastEditors: lmio 2091319361@qq.com
Description: 100266. 交替子数组计数
'''

import math
from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        left, right = 0, 1
        res = 0
        n = len(nums)
        while right < n:
            while right < n and nums[right] != nums[right-1]:
                right += 1
            l = right-left
            res += (l*(1+l))//2
            left = right
            right += 1
        return res+1 if left == n-1 else res