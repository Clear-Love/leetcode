'''
Author: lmio 2091319361@qq.com
Date: 2023-08-07 13:41:37
LastEditors: lmio 2091319361@qq.com
Description: 面试题 08.01. 三步问题
'''

class Solution:
    def waysToStep(self, n: int) -> int:
        MOD = 1000000007
        dp = [1, 1, 2, 4]
        if n < 4:
            return dp[n]
        for i in range(4, n+1):
            dp.append((dp[i-1] + dp[i-2] + dp[i-3]) % MOD)
        return dp[-1] % MOD