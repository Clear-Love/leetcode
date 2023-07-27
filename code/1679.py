'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 20:38:00
LastEditors: lmio 2091319361@qq.com
Description: 1679. K 和数对的最大数目
'''

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        res = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum == k:
                res += 1
                left += 1
                right -= 1
            elif sum < k:
                left += 1
            else:
                right -= 1
        return res