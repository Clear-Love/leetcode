'''
Author: lmio 2091319361@qq.com
Date: 2023-08-17 22:25:43
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.24. 数对和
'''

from collections import defaultdict
from typing import List


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        m = defaultdict(int)
        res = []
        for v in nums:
            if m[target-v]:
                res.append([target-v, v])
                m[target-v] -= 1
            else:
                m[v] += 1
        return res