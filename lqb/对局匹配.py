'''
Author: lmio 2091319361@qq.com
Date: 2024-05-28 14:26:31
LastEditors: lmio 2091319361@qq.com
Description: 对局匹配
'''

import sys
from typing import Counter

n, k = list(map(int, input().split()))
ranks = list(map(int, input().split()))
cnts = Counter(ranks)
N = max(ranks)+1

group = [[] for _ in range(k)]

if k == 0:
    print(len(cnts))
    sys.exit(0)

res = 0

for i in range(k):
    ans = 0
    group = []
    for j in range(i, N, k):
        group.append(cnts[j])
    dp = [0]*len(group)
    dp[0] = group[0]
    dp[1] = max(group[0], group[1])
    for j in range(2, len(group)):
        # j 选或者不选
        dp[j] = max(dp[j-1], dp[j-2]+group[j])
    res += dp[-1]
print(res)