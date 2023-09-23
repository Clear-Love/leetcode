'''
Author: lmio 2091319361@qq.com
Date: 2023-09-10 10:30:34
LastEditors: lmio 2091319361@qq.com
Description: 8029. 与车相交的点
'''

import enum
from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        if not nums:
            return 0
        res = 0
        nums.sort()
        start, end = nums[0]
        for u, v in nums:
            if u <= end:
                end = max(end, v)
            else:
                res += end - start + 1
                start, end = u, v
        res += end-start+1
        return res