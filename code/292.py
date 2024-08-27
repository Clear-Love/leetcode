'''
Author: lmio 2091319361@qq.com
Date: 2024-03-16 18:33:02
LastEditors: lmio 2091319361@qq.com
Description: 292. Nim 游戏
'''

from functools import cache


class Solution:
    def canWinNim(self, n: int) -> bool:
        
        @cache
        def canWin(c: int) -> bool:
            if c <= 3:
                return True
            return not (canWin(c-1) and canWin(c-2) and canWin(c-3))
        return canWin(n)