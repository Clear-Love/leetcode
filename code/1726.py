'''
Author: lmio 2091319361@qq.com
Date: 2023-10-19 12:38:20
LastEditors: lmio 2091319361@qq.com
Description: 1726. 同积元组
'''


from collections import defaultdict
from itertools import combinations
import math
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        cnts = defaultdict(int)
        for x, y in combinations(nums, 2):
            cnts[x*y] += 1
        res = 0
        for n in cnts.values():
            if n >= 2:
                res += math.comb(n, 2)*8
        return res