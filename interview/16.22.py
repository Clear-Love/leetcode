'''
Author: lmio 2091319361@qq.com
Date: 2023-08-17 21:33:00
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.22. 兰顿蚂蚁
'''

from typing import List


class Solution:
    def printKMoves(self, K: int) -> List[str]:
        black = set()
        d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        faces = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}
        maxx, maxy, minx, miny = 0, 0, 0, 0
        face = 0
        x, y = 0, 0
        for _ in range(K):
            if (x, y) in black:
                face = (face-1)%4
                black.remove((x, y))
            else:
                face = (face+1)%4
                black.add((x, y))
            x, y = x + d[face][0], y + d[face][1]
            maxx = max(maxx, x)
            maxy = max(maxy, y)
            minx = min(minx, x)
            miny = min(miny, y)
        n, m = max(1, maxx - minx+1), max(1, maxy - miny+1)
        res = [['_' for _ in range(n)] for _ in range(m)]
        for i, j in black:
            res[m-j-miny][i-minx] = 'X'
        res[y-miny][x-minx] = faces[face]
        for i in range(m):
            res[i] = ''.join(res[i])
        return res