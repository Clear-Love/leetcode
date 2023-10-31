'''
Author: lmio 2091319361@qq.com
Date: 2023-10-27 16:43:17
LastEditors: lmio 2091319361@qq.com
Description: 1475. 商品折扣后的最终价格
'''

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []
        res = [0]*n
        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                res[stack.pop()] = p
            stack.append(i)
        return [prices[i]-res[i] for i in range(n)]