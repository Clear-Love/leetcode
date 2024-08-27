'''
Author: lmio 2091319361@qq.com
Date: 2024-05-28 11:34:05
LastEditors: lmio 2091319361@qq.com
Description: 发现环
'''

from collections import defaultdict, deque


n = int(input())

deg = [0] * (n+1) # 记录每个点的入度
g = defaultdict(list)

for i in range(n):
    a, b = list(map(int, input().split()))
    g[a].append(b)
    g[b].append(a)
    deg[b] += 1
    deg[a] += 1

q = deque(i for i in range(1, n+1) if deg[i] == 1)
vis = [False] * (n+1)
while q:
    x = q.popleft()
    vis[x] = True
    for y in g[x]:
        if vis[y]:
            continue
        deg[y] -= 1
        if deg[y] == 1:
            q.append(y)

res = sorted([i for i in range(1, n+1) if not vis[i]])

print(" ".join(list(map(str, res))))