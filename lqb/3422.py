'''
Author: lmio 2091319361@qq.com
Date: 2024-04-02 22:28:59
LastEditors: lmio 2091319361@qq.com
Description: 3422. 左孩子右兄弟
'''

from collections import defaultdict
from functools import cache


n =  int(input())
g = defaultdict(list)
for i in range(2, n+1):
    parent = int(input())
    g[parent].append(i)
@cache
def dfs(i: int):
    res = 0
    n = len(g[i])
    for j in g[i]:
        res = max(res, dfs(j)+n)
    return res
print(dfs(1))