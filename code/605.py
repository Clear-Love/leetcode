'''
Author: lmio 2091319361@qq.com
Date: 2023-07-27 17:13:58
LastEditors: lmio 2091319361@qq.com
Description: 605. 种花问题
'''

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def isFlowered(i: int):
            if i < 0 or i >= len(flowerbed):
                return False
            return flowerbed[i]
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if not isFlowered(i-1) and not isFlowered(i+1):
                flowerbed[i] = 1
                n -= 1
        return n <= 0