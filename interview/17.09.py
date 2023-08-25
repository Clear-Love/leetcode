'''
Author: lmio 2091319361@qq.com
Date: 2023-08-21 21:51:20
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.09. 第 k 个数
'''

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [1] * k
        p3, p5, p7 = 0, 0, 0
        for i in range(1, k):
            a, b, c = dp[p3]*3, dp[p5]*5, dp[p7]*7
            v = min(a, b, c)
            dp[i] = v
            if v == a:
                p3 += 1
            if v == b:
                p5 += 1
            if v == c:
                p7 += 1
        return dp[k-1]