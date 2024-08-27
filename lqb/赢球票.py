'''
Author: lmio 2091319361@qq.com
Date: 2024-05-28 11:14:31
LastEditors: lmio 2091319361@qq.com
Description: 赢球票
'''

import os
import sys

# 请在此输入您的代码
n = int(input())
crads = list(map(int, input().split()))

res = 0
for i in range(n):
    idx = i
    vis = set()
    c = 1 # 数数
    while c <= n:
        if len(vis) == n:
            break
        while crads[idx] in vis:
            idx = (idx + 1) % n
        if c not in vis and crads[idx] == c:
            vis.add(c)
            c = 0
        c += 1
        idx = (idx + 1) % n
    res = max(res, sum(vis))
print(res)