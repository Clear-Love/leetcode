'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 20:33:29
LastEditors: lmio 2091319361@qq.com
Description: 11. 盛最多水的容器
'''

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = 0
        while left < right:
            hl, hr = height[left], height[right]
            if hl < hr:
                res = max(res, (right-left)*hl)
                left += 1
            else:
                res = max(res, (right-left)*hr)
                right -= 1
        return res