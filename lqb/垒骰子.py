'''
Author: lmio 2091319361@qq.com
Date: 2024-05-29 09:45:24
LastEditors: lmio 2091319361@qq.com
Description: 垒骰子
'''

n, m = list(map(int, input().split()))

face = [0, 4, 5, 6, 1, 2, 3]

dis = [set() for _ in range(7)]

for i in range(m):
    a, b = list(map(int, input().split()))
    dis[face[b]].add(a)
    dis[face[a]].add(b)

MOD = 10**9 + 7


# 表示垒到第i个骰子有多少种情况
dp = [[0]*7 for _ in range(n)]

for i in range(1, 7):
    dp[0][i] = 4
for i in range(n):
    for j in range(1, 7):
        for k in range(1, 7):
            if k not in dis[j]:
                # 骰子j可以垒到骰子k上
                dp[i][j] += dp[i-1][k]*4%MOD

print(sum(dp[-1])%MOD)