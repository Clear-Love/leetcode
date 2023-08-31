'''
Author: lmio 2091319361@qq.com
Date: 2023-08-29 17:14:22
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.23. 最大黑方阵
'''

from collections import defaultdict
from typing import List

class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        mxrow = defaultdict(int)
        mxcol = defaultdict(int)
        n = len(matrix)
        res = []
        for r in range(n-1, -1, -1):
            for c in range(n-1, -1, -1):
                if matrix[r][c] == 0:
                    mxrow[r, c] = 1 + mxrow[r, c + 1]
                    mxcol[r, c] = 1 + mxcol[r + 1, c]
        for r in range(n):
            for c in range(n):
                if matrix[r][c] == 0:
                    mxsize = min(mxrow[r, c], mxcol[r, c])
                    cursize = 0 if not res else res[2]
                    for size in range(mxsize, cursize, -1):
                        if mxcol[r, c + size - 1] >= size and mxrow[r + size - 1, c] >= size:
                            res = [r, c, size]
                            break
        return res