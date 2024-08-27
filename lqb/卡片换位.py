'''
Author: lmio 2091319361@qq.com
Date: 2024-05-31 14:37:29
LastEditors: lmio 2091319361@qq.com
Description: 卡片换位
'''

from collections import deque
from typing import List


diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]

n, m = 2, 3
start = input() + input()

def get(g: str) -> List[int]:
    res = [0]*3
    for i, w in enumerate(g):
        if w == 'A':
            res[0] = i
        elif w == 'B':
            res[1] = i
        elif w == ' ':
            res[2] = i
    return res

aIdx, bIdx, space = get(start)

q = deque([(0, start)])

vis = set()

while q:
    dist, g = q.popleft()
    if g in vis:
        continue
    a, b, s = get(g)
    vis.add(g)
    # 成功交换位置
    if (a, b) == (bIdx, aIdx):
        print(dist)
        break
    x, y = divmod(s, m)
    # 向空格移动
    for dx, dy in diff:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        tmp = list(g)
        tmp[nx*m+ny], tmp[x*m+y] = tmp[x*m+y], tmp[nx*m+ny]
        q.append((dist+1, ''.join(tmp)))