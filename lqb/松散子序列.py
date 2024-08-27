'''
Author: lmio 2091319361@qq.com
Date: 2024-04-09 18:53:40
LastEditors: lmio 2091319361@qq.com
Description: 松散子序列
'''

s = input()
n = len(s)
def value(s: str) -> int:
    return ord(s) - ord('a')+1
dp = [[0, 0] for _ in range(n)]
dp[0] = (value(s[0]), 0)
for i in range(1, n):
    # 选
    dp[i][0] = dp[i-1][1]+value(s[i])
    # 不选
    dp[i][1] = max(dp[i-1])
print(max(dp[-1]))