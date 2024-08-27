'''
Author: lmio 2091319361@qq.com
Date: 2024-05-29 16:58:49
LastEditors: lmio 2091319361@qq.com
Description: 生命之树
'''
 
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

n = int(input()) # 生命之树
vals = [0] + list(map(int, input().split())) # 每个节点的值

g = defaultdict(list) # 邻接表

for i in range(n-1):
    u, v = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)

res = 0

def dfs(i: int, fa: int) -> int:
    global res
    ans = vals[i]
    for j in g[i]:
        if j != fa:
            ans = max(ans, ans+dfs(j, i))
    res = max(res, ans)
    return ans
dfs(1, -1)
print(res)