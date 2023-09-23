'''
Author: lmio 2091319361@qq.com
Date: 2023-09-19 20:10:04
LastEditors: lmio 2091319361@qq.com
Description: 2517. 礼盒的最大甜蜜度
'''

from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)
        # 甜蜜度为t可以选择多少类糖果
        def fn(t: int) -> int:
            pre = price[0]
            cnt = 1
            for p in price:
                if p-pre >= t:
                    cnt += 1
                    pre = p
            return cnt
        l, r = 0, price[-1]-price[0]
        while l < r:
            mid = (l+r+1) >> 1
            if fn(mid) < k:
                r = mid-1
            else:
                l = mid
        return l