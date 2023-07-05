'''
Author: lmio 2091319361@qq.com
Date: 2023-07-05 19:21:50
LastEditors: lmio 2091319361@qq.com
Description: 73. 矩阵置零
'''

from typing import List

def setZeroes(matrix: List[List[int]]) -> None:
    row = set()
    col = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
    for v in row:
        for j in range(len(matrix[v])):
            matrix[v][j] = 0
    for v in col:
        for i in range(len(matrix)):
            matrix[i][v] = 0