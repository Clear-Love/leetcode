'''
Author: lmio 2091319361@qq.com
Date: 2024-05-31 16:54:32
LastEditors: lmio 2091319361@qq.com
Description: 近似gcd
'''

import bisect


n, g = list(map(int, input().split()))

nums = list(map(int, input().split()))

preCnt = [0]

for num in nums:
    if num%g != 0:
        preCnt.append(preCnt[-1]+1)
    else:
        preCnt.append(preCnt[-1])

cnt = 0

for i in range(n):
    target = 1 + preCnt[i]
    r = bisect.bisect_right(preCnt, target)
    cnt += r-i-2

print(cnt)