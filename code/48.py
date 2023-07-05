'''
Author: lmio 2091319361@qq.com
Date: 2023-07-05 19:18:50
LastEditors: lmio 2091319361@qq.com
Description: 48. 旋转图像
'''
from typing import List

def rotate(matrix: List[List[int]]) -> None:
    # 转置矩阵
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # 翻转每一行
    for i in range(n):
        matrix[i] = matrix[i][::-1]