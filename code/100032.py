'''
Author: lmio 2091319361@qq.com
Date: 2023-09-30 22:37:32
LastEditors: lmio 2091319361@qq.com
Description: 100032. 使数组为空的最少操作次数
'''

from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnts = Counter(nums)
        res = 0
        for cnt in cnts.values():
            if cnt == 1:
                return -1
            c, m = divmod(cnt, 3)
            if m == 0:
                res += c
            else:
                res += c+1
        return res