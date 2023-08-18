'''
Author: lmio 2091319361@qq.com
Date: 2023-08-18 22:24:13
LastEditors: lmio 2091319361@qq.com
Description: 974. 和可被 K 整除的子数组
'''

from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        m = defaultdict(int)
        m[0] = 1
        s = 0
        for num in nums:
            s += num
            mod = s%k
            res += m[mod]
            m[mod] += 1
        return res