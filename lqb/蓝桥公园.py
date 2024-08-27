'''
Author: lmio 2091319361@qq.com
Date: 2024-05-31 20:24:11
LastEditors: lmio 2091319361@qq.com
Description: 蓝桥公园
'''

from math import inf


n, m, q = list(map(int, input().split()))

dp = [[inf] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = 0

for _ in range(m):
    u, v, w = list(map(int, input().split()))
    dp[u][v] = min(dp[u][v], w)
    dp[v][u] = min(dp[v][u], w)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for _ in range(q):
    start, end = list(map(int, input().split()))
    if dp[start][end] == inf:
        print(-1)
    else:
        print(dp[start][end])