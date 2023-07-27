'''
Author: lmio 2091319361@qq.com
Date: 2023-07-24 22:35:22
LastEditors: lmio 2091319361@qq.com
Description: 771. 宝石与石头
'''
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        res = 0
        for ch in stones:
            if ch in jewels:
                res += 1
        return res