'''
Author: lmio 2091319361@qq.com
Date: 2023-09-18 15:46:54
LastEditors: lmio 2091319361@qq.com
Description: 2861. 最大合金数
'''

from typing import List


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        mx = min(stock) + budget
        res = 0
        for com in composition:
            c = sum([com[i]*cost[i] for i in range(n)])
            def check(cnt: int) -> bool:
                m = cnt*c
                for i, v in enumerate(stock):
                    m -= cost[i]*min(cnt*com[i], v)
                return m <= budget
            l = budget//c
            r = mx+1
            while l < r:
                mid = (l+r+1) >> 1
                if check(mid):
                    l = mid
                else:
                    r = mid-1
            res = max(res, l)
        return res