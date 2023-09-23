'''
Author: lmio 2091319361@qq.com
Date: 2023-09-18 11:52:49
LastEditors: lmio 2091319361@qq.com
Description: 2859. 计算 K 置位下标对应元素的和
'''

from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def valid(num: int) -> bool:
            for _ in range(k):
                if num == 0:
                    return False
                num = num&(num-1)
            return num == 0
        res = 0
        for i, v in enumerate(nums):
            if valid(i):
                res += v
        return res