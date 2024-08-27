'''
Author: lmio 2091319361@qq.com
Date: 2024-05-11 17:08:55
LastEditors: lmio 2091319361@qq.com
Description: 2391. 收集垃圾的最少总时间
'''

from itertools import accumulate
from typing import Counter, List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = sum(map(len, garbage)) + sum(travel) * 3
        print(list(zip(reversed(garbage), reversed(travel))))
        for c in "MPG":
            # 倒序遍历，找到最后一个出现的
            for g, t in zip(reversed(garbage), reversed(travel)):
                if c in g:
                    break
                res -= t
        return res