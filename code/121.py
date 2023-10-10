'''
Author: lmio 2091319361@qq.com
Date: 2023-10-01 18:40:02
LastEditors: lmio 2091319361@qq.com
Description: 121. 买卖股票的最佳时机
'''

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        res = 0
        for i in range(1, len(prices)):
            v = prices[i]
            res = max(res, v-minPrice)
            minPrice = min(minPrice, v)
        return res