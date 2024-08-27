'''
Author: lmio 2091319361@qq.com
Date: 2024-04-11 08:41:44
LastEditors: lmio 2091319361@qq.com
Description: 最小质因子之和
'''

# 得到1~n的最小质因数之和
from typing import List


def get(n) -> List[int]:
    mFact = [0]*(n+1)
    isPri = [True]*(n+1)
    pri = []
    for i in range(2, n+1):
        if isPri[i]:
            pri.append(i)
            mFact[i] = i
        for j in pri:
            if i*j > n:
                break
            isPri[i*j] = False
            mFact[i*j] = j
            if i % j == 0:
                break
    preSum = [0]*(n+1)
    for i in range(2, n+1):
        preSum[i] = preSum[i-1] + mFact[i]
    return preSum

t = int(input())
q = []
n = 0
for _ in range(t):
    v = int(input())
    n = max(n, v)
    q.append(v)
preSum = get(n)
for v in q:
    print(preSum[v])