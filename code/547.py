'''
Author: lmio 2091319361@qq.com
Date: 2023-10-09 23:18:13
LastEditors: lmio 2091319361@qq.com
Description: 547. 省份数量
'''

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        res = 0
        def dfs(x, y):
            if isConnected[x][y] != 1:
                return
            isConnected[x][y] = 0
            for i in range(n):
                dfs(y, i)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    res += 1
                    dfs(i, j)
        return res