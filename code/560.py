'''
Author: lmio 2091319361@qq.com
Date: 2023-08-18 22:12:17
LastEditors: lmio 2091319361@qq.com
Description: 560. 和为 K 的子数组
'''

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = 0
        res = 0
        m = defaultdict(int)
        m[0] = 1
        for num in nums:
            s += num
            res += m[s-k]
            m[s] += 1
        return res