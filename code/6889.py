'''
Author: lmio 2091319361@qq.com
Date: 2023-07-16 19:44:56
LastEditors: lmio 2091319361@qq.com
Description: 6889. 特殊元素平方和
'''
from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i, v in enumerate(nums):
            if n%(i+1) == 0:
                res += v*v
        return res