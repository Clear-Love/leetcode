'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 17:09:46
LastEditors: lmio 2091319361@qq.com
Description: 1431. 拥有最多糖果的孩子
'''

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False] * len(candies)
        maxCandy = max(candies)
        for i, v in enumerate(candies):
            if v + extraCandies >= maxCandy:
                res[i] = True
        return res