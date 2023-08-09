'''
Author: lmio 2091319361@qq.com
Date: 2023-08-09 15:05:01
LastEditors: lmio 2091319361@qq.com
Description: 面试题 08.10. 颜色填充
'''

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        color = image[sr][sc]
        visited = set()
        def dfs(x: int, y: int):
            image[x][y] = newColor
            for dx, dy in d:
                nx, ny = x+dx, y+dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and image[nx][ny] == color and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    dfs(nx, ny)
                    visited.remove((nx, ny))
        dfs(sr, sc)
        return image