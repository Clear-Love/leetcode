'''
Author: lmio 2091319361@qq.com
Date: 2023-08-12 21:41:05
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.10. 生存人数
'''

from collections import defaultdict
from typing import List


class Solution:
    def maxAliveYear(self, birth: List[int], death: List[int]) -> int:
        inc = defaultdict(int)
        n = len(birth)
        for i in range(n):
            inc[birth[i]] += 1
            inc[death[i]+1] -= 1
        years = list(inc.keys())
        years.sort()
        res = years[0]
        cnt = 0
        s = 0
        for year in years:
            s += inc[year]
            if s > cnt:
                res = year
                cnt = s
        return res