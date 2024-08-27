'''
Author: lmio 2091319361@qq.com
Date: 2024-04-08 09:30:26
LastEditors: lmio 2091319361@qq.com
Description: 123
'''
import bisect


N = 1500000
preSum = [0 for _ in range(N)]
ids = [0 for _ in range(N)]
for i in range(1, N):
    s = i*(i+1)//2
    preSum[i] = preSum[i-1] + s
    ids[i] = ids[i-1] + i
t = int(input())

def fs(i: int) -> int:
    if i == 0:
        return 0
    idx = bisect.bisect_left(ids, i)-1
    n = i - ids[idx]
    return preSum[idx] + n*(1+n)//2

for _ in range(t):
    l, r = list(map(int, input().split()))
    print(fs(r)-fs(l-1))