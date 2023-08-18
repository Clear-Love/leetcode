'''
Author: lmio 2091319361@qq.com
Date: 2023-08-19 00:04:37
LastEditors: lmio 2091319361@qq.com
Description: 525. 连续数组
'''

from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = 0
        res = 0
        m = {0: -1}
        for i, v in enumerate(nums):
            s += v if v else -1
            print(s)
            if s in m:
                res = max(res, i-m[s])
            else:
                m[s] = i
        return res