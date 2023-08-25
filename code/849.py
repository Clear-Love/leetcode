'''
Author: lmio 2091319361@qq.com
Date: 2023-08-22 16:00:47
LastEditors: lmio 2091319361@qq.com
Description: 849. 到最近的人的最大距离
'''

from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        f = [0]*n
        f[0] = 0 if seats[0] else n
        for i in range(1, n):
            if seats[i] == 1:
                continue
            f[i] = f[i-1] + 1
        dp = [0]*n
        dp[n-1] = 0 if seats[n-1] else n
        res = max(0, min(dp[n-1], f[n-1]))
        for i in range(n-2, -1, -1):
            if seats[i] == 1:
                continue
            dp[i] = dp[i+1]+1
            res = max(res, min(dp[i], f[i]))
        return res