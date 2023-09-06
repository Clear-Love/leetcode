'''
Author: lmio 2091319361@qq.com
Date: 2023-09-02 14:11:16
LastEditors: lmio 2091319361@qq.com
Description: 32. 最长有效括号
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[0, 0] for _ in range(n+1)]
        for i, ch in enumerate(s, start=1):
            if ch == ')':
                if dp[i-1][1] == 0:
                    continue
                dp[i][0] = dp[i-1][0] + 2
                dp[i][1] = dp[i-1][1] - 1
                dp[i][0] += dp[i-dp[i][0]][0]
            else:
                dp[i][0] = 0
                dp[i][1] = dp[i-1][1] + 1
            res = max(res, dp[i][0])
        return res