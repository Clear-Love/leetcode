'''
Author: lmio 2091319361@qq.com
Date: 2023-07-31 20:47:00
LastEditors: lmio 2091319361@qq.com
Description: 901. 股票价格跨度
'''

from collections import deque


class StockSpanner:

    def __init__(self):
        self.stack = deque()

    def next(self, price: int) -> int:
        stack = self.stack
        res = 1
        while stack and price >= stack[-1][0]:
            _, past = stack.pop()
            res += past
        stack.append((price, res))
        return res