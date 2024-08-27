'''
Author: lmio 2091319361@qq.com
Date: 2024-04-09 20:06:31
LastEditors: lmio 2091319361@qq.com
Description: 管道
'''

from math import inf


n, length = list(map(int, input().split()))
grep = []
left, right = 0, 0
for _ in range(n):
    grep.append(list(map(int, input().split())))
    right = max(right, grep[-1][1])
right += n
def check(t: int) -> bool:
    global grep, length
    m = set(range(1, length+1))
    for li, si in grep:
        if t >= si:
            l = max(1, li-t+si)
            r = min(length, li+t-si)
            for v in range(l, r+1):
                m.discard(v)
    return len(m) == 0
while left < right:
    mid = (left+right) >> 1
    if check(mid):
        right = mid
    else:
        left = mid+1
print(left)