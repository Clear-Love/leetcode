'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 17:34:30
LastEditors: lmio 2091319361@qq.com
Description: 334. 递增的三元子序列
'''

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = [float('inf')] * 3
        for num in nums:
            if num > f[1]:
                return True
            elif f[0] < num < f[1]:
                f[1] = num
            elif num < f[0]:
                f[0] = num
        return False