'''
Author: lmio 2091319361@qq.com
Date: 2024-04-01 03:22:46
LastEditors: lmio 2091319361@qq.com
Description: 
'''

from functools import cache

n, m, k = list(map(int, input().split()))
@cache
def dfs(i: int, c: int) -> int:
    # 从i街道开始，剩余c资金
    if i == n:
        return min(m, c)
    ans = 0
    for j in range(1, min(m+1, c)):
        ans += dfs(i+1, c-j)
    return ans
print(0xffff & 16)