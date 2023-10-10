'''
Author: lmio 2091319361@qq.com
Date: 2023-10-08 21:36:28
LastEditors: lmio 2091319361@qq.com
Description: 8028. 执行操作使两个字符串相等
'''

class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        diff = []
        for i in range(n):
            if s1[i] != s2[i]:
                diff.append(i)
        n = len(diff)
        if n == 0:
            return 0
        if n&1:
            return -1
        dp = [0]*(n+1)
        dp[1] = x
        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+x, dp[i-2]+(diff[i-1]-diff[i-2])*2)
        return dp[-1]//2