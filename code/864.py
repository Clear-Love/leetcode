'''
Author: lmio 2091319361@qq.com
Date: 2023-10-15 14:49:00
LastEditors: lmio 2091319361@qq.com
Description: 864. 获取所有钥匙的最短路径
'''

from collections import deque
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        # x, y, cur_keys
        n, m = len(grid), len(grid[0])
        q = deque()
        key_sum = 0
        for i in range(n):
            for j in range(m):
                ch = grid[i][j]
                if ch == '@':
                    q.append((i, j, 0, 0))
                elif ch.islower():
                    key_sum ^= (1 << (ord(ch) - ord('a')))
        vis = set(q)
        d = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while q:
            x, y, s, step = q.popleft()
            if s == key_sum:
                return step
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and grid[nx][ny] != '#' and (nx, ny, s) not in vis:
                    vis.add((nx, ny, s))
                    ch = grid[nx][ny]
                    # 钥匙
                    if ch.islower():
                        pos = 1 << (ord(ch)-ord('a'))
                        # 已经拿过钥匙
                        if s&pos:
                            q.append((nx, ny, s, step+1))
                        else:
                            if s^pos == key_sum:
                                return step+1
                            q.append((nx, ny, s^pos, step+1))
                    # 锁
                    elif ch.isupper():
                        pos = 1 << (ord(ch)-ord('A'))
                        # 有对应钥匙
                        if s&pos:
                            q.append((nx, ny, s, step+1))
                    else:
                        q.append((nx, ny, s, step+1))
        return -1