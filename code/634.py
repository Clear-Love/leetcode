'''
Author: lmio 2091319361@qq.com
Date: 2023-09-02 19:54:04
LastEditors: lmio 2091319361@qq.com
Description: 634. 寻找数组的错位排列
'''

class Solution:
    def findDerangement(self, n: int) -> int:
        MOD = 10**9+7
        if n == 1:
            return 0
        if n == 2:
            return 1
        dp = [0]*n
        dp[1] = 1
        for i in range(2, n):
            dp[i] = ((dp[i-1] + dp[i-2])*i)%MOD
        return dp[-1]