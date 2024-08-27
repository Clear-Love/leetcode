'''
Author: lmio 2091319361@qq.com
Date: 2024-05-31 17:11:56
LastEditors: lmio 2091319361@qq.com
Description: 交通信号
'''

from collections import defaultdict
import heapq
from math import inf
import sys


n, m, s, t = list(map(int, input().split()))

cycles = ['g', 'y', 'r', 'y']

graph = defaultdict(list)

# 当信号灯为绿灯时允许正向通行, 红灯时允许反向通行, 
# 黄灯时不 允许通行。
# 每条边上的信号灯的三种颜色的持续时长都互相独立, 其中黄灯的 持续时长等同于走完路径的耗时。
for _ in range(m):
    u, v, g, r, d = list(map(int, input().split()))
    c = d*2+g+r #红绿灯周期
    graph[u].append((v, g, r, d, c, False))
    graph[v].append((u, g, r, d, c, True))

# s 到结点 t 所需的最短时间

q = [(0, s)]
vis = set()
dist_ = [inf]*(n+1)
while(q):
    dist, x = heapq.heappop(q)
    if x in vis:
        continue
    vis.add(x)
    if x == t:
        print(dist)
        sys.exit(0)
    for y, g, r, d, c, isReverse in graph[x]:
        remain = dist%c
        w = d
        # 需要等待这一轮的, 如果反向，红灯可以通行
        if isReverse:
            if remain >= g+d+r:
                w += c-remain+g+d
            elif remain < g+d:
                w += g+d-remain
        else:
            if remain >= g:
                w += c-remain
        if dist_[y] > dist+w:
            dist_[y] = dist+w
            heapq.heappush(q, (dist+w, y))