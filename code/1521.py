'''
Author: lmio 2091319361@qq.com
Date: 2024-04-01 15:06:36
LastEditors: lmio 2091319361@qq.com
Description: 1521. 找到最接近目标值的函数值
'''

from math import inf
from typing import List


class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        d = set()
        res = inf
        for num in arr:
            d = {v&num for v in d}
            d.add(num)
            res = min(res, min(abs(v-target) for v in d))
        return res