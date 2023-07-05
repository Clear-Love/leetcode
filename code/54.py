'''
Author: lmio 2091319361@qq.com
Date: 2023-07-05 17:27:17
LastEditors: lmio 2091319361@qq.com
Description: 54. 螺旋矩阵
'''

from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    m, n = len(matrix), len(matrix[0])
    res = []
    for level in range(min(m, n)//2):
        for j in range(level, n-level):
            res.append(matrix[level][j])

        for i in range(level+1, m-level):
            res.append(matrix[i][n-level-1])

        for j in range(n-level-2, level-1, -1):
            res.append(matrix[m-level-1][j])

        for i in range(m-level-2, level, -1):
            res.append(matrix[i][level])

    if min(m, n)%2 == 1:
        level = min(m, n)//2
        if m<=n:
            for j in range(level, n-level):
                res.append(matrix[level][j])
        else:
            for i in range(level, m-level):
                res.append(matrix[i][n-level-1])
    return res