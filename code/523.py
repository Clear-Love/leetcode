'''
Author: lmio 2091319361@qq.com
Date: 2023-08-18 23:53:25
LastEditors: lmio 2091319361@qq.com
Description: 523. 连续的子数组和
'''

from collections import defaultdict
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m = {}
        m[0] = -1
        s = 0
        for i, num in enumerate(nums):
            s += num
            mod = s%k
            if mod in m:
                if i - m[mod] >= 2:
                    return True
            else:
                m[mod] = i
        return False