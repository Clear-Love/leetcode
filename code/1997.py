'''
Author: lmio 2091319361@qq.com
Date: 2024-03-28 20:51:31
LastEditors: lmio 2091319361@qq.com
Description: 1997. 访问完所有房间的第一天
'''

from typing import List


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        if n == 1:
            return 0
        dp = [0]*n
        for i in range(1, n):
            dp[i] = 2*dp[i-1] - dp[nextVisit[i-1]]+1
        return dp[-1]+1