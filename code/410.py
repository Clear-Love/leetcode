'''
Author: lmio 2091319361@qq.com
Date: 2023-10-24 15:41:57
LastEditors: lmio 2091319361@qq.com
Description: 410. 分割数组的最大值
'''

from functools import cache
from itertools import accumulate
from math import inf
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def check(mx: int) ->bool:
            i = 0
            c = 0
            while i < n:
                if c == k:
                    return False
                s = 0
                while i < n and s + nums[i] <= mx:
                    s += nums[i]
                    i += 1
                c += 1
            return True
        left, right = 0, sum(nums)
        while left < right:
            mid = (left+right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left

s = Solution()
print(s.splitArray([7,2,5,10,8], 2))