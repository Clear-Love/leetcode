'''
Author: lmio 2091319361@qq.com
Date: 2023-09-05 14:44:52
LastEditors: lmio 2091319361@qq.com
Description: 954. 二倍数对数组
'''

from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnts = Counter(arr)
        if cnts[0]&1 != 0:
            return False
        for v in sorted(cnts, key=abs):
            if cnts[2*v] < cnts[v]:
                return False
            cnts[2*v] -= cnts[v]
        return True