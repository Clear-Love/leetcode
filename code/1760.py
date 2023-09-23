'''
Author: lmio 2091319361@qq.com
Date: 2023-09-22 21:08:28
LastEditors: lmio 2091319361@qq.com
Description: 1760. 袋子里最少数目的球
'''

from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left+right) >> 1
            if sum([(v-1)//mid for v in nums]) > maxOperations:
                left = mid+1
            else:
                right = mid
        return left