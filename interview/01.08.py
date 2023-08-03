'''
Author: lmio 2091319361@qq.com
Date: 2023-08-03 09:31:01
LastEditors: lmio 2091319361@qq.com
Description: 面试题 01.08. 零矩阵
'''

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for r in row:
            for j in range(len(matrix[r])):
                matrix[r][j] = 0
        for c in col:
            for i in range(len(matrix)):
                matrix[i][c] = 0