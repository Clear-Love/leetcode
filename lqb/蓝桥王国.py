'''
Author: lmio 2091319361@qq.com
Date: 2024-04-10 10:08:16
LastEditors: lmio 2091319361@qq.com
Description: 蓝桥王国
'''

import heapq


n, m = list(map(int, input().split()))

g = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = list(map(int, input().split()))
    g[u].append((v, w))
res = [0]*(n+1)
q = [(0, 1)]
vis = set()
while q:
    d, x = heapq.heappop(q)
    if x in vis:
        continue
    vis.add(x)
    res[x] = d
    for y, w in g[x]:
        heapq.heappush(q, (d+w, y))
print(' '.join(map(str, res[1:])))