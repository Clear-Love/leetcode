'''
Author: lmio 2091319361@qq.com
Date: 2023-09-20 21:38:20
LastEditors: lmio 2091319361@qq.com
Description: 2439. 最小化数组中的最大值
'''

from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(d: int) ->bool:
            remain = 0
            for v in nums:
                if v > d:
                    if v-d > remain:
                        return False
                    remain -= v-d
                else:
                    remain += d-v
            return True
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left