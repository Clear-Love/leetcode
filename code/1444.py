'''
Author: lmio 2091319361@qq.com
Date: 2023-08-17 14:10:02
LastEditors: lmio 2091319361@qq.com
Description: 1444. 切披萨的方案数
'''

from typing import List


class Solution:
    def ways(self, pizza: List[str], cnt: int) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(pizza), len(pizza[0])
        apples = [[0] * (n + 1) for _ in range(m + 1)]
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(cnt)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                apples[i][j] = apples[i][j + 1] + apples[i + 1][j] - apples[i + 1][j + 1] + (pizza[i][j] == 'A')
                dp[0][i][j] = 1 if apples[i][j] > 0 else 0
        for k in range(1, cnt):
            for i in range(m):
                for j in range(n):
                    # 水平方向
                    for i2 in range(i + 1, m):
                        # 可以切
                        if apples[i][j] > apples[i2][j]:
                            dp[k][i][j] = (dp[k][i][j] + dp[k-1][i2][j]) % MOD
                    # 垂直方向
                    for j2 in range(j + 1, n):
                        if apples[i][j] > apples[i][j2]:
                            dp[k][i][j] = (dp[k][i][j] + dp[k-1][i][j2]) % MOD
        return dp[cnt-1][0][0]