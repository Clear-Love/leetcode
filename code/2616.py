'''
Author: lmio 2091319361@qq.com
Date: 2023-09-20 22:39:30
LastEditors: lmio 2091319361@qq.com
Description: 2616. 最小化数对的最大差值
'''

from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums.sort()
        n = len(nums)
        def check(d: int) ->bool:
            cnt = 0
            i = 1
            while i < n:
                if nums[i] - nums[i-1] <= d:
                    cnt += 1
                    if cnt >= p:
                        return True
                    i += 1
                i += 1
            return False
        left, right = 0, nums[-1]-nums[0]
        while left < right:
            mid = (left+right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid+1
        return left