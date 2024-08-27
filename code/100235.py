'''
Author: lmio 2091319361@qq.com
Date: 2024-03-31 10:42:51
LastEditors: lmio 2091319361@qq.com
Description: 100235. 换水问题 II
'''

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = 0
        res = 0
        while numBottles:
            res += numBottles
            emptyBottles += numBottles
            numBottles = 0
            if emptyBottles < numExchange:
                break
            numBottles += 1
            emptyBottles -= numExchange
            numExchange += 1
        return res