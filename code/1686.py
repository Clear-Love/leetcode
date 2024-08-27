'''
Author: lmio 2091319361@qq.com
Date: 2024-03-16 16:02:55
LastEditors: lmio 2091319361@qq.com
Description: 1686. 石子游戏 VI
'''

from typing import List


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        values = list(zip(aliceValues, bobValues))
        values.sort(reverse=True, key=lambda x: x[0]+x[1])
        av, bv = 0, 0
        for i in range(len(values)):
            if i&1 == 0:
                av += values[i][0]
            else:
                bv += values[i][1]
        if av == bv:
            return 0
        elif av > bv:
            return 1
        else:
            return -1