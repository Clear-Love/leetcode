'''
Author: lmio 2091319361@qq.com
Date: 2023-09-30 22:48:10
LastEditors: lmio 2091319361@qq.com
Description: 100019. 将数组分割成最多数目的子数组
'''

from typing import List


class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        tar = 0
        def check(c: int) ->bool:
            s = nums[0]
            i = 1
            cnt = 1
            while i < n:
                while i < n and s > tar:
                    s &= nums[i]
                    i += 1
                if i >= n:
                    break
                cnt += 1
                s = nums[i]
                i += 1
                if cnt == c:
                    break
            while i < n:
                s &= nums[i]
                i += 1
            return cnt >=c and s <= tar
        left, right = 1, n
        while left < right:
            mid = (left+right+1) >> 1
            if check(mid):
                left = mid
            else:
                right = mid-1
        return left