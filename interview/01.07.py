'''
Author: lmio 2091319361@qq.com
Date: 2023-08-03 09:24:49
LastEditors: lmio 2091319361@qq.com
Description: 面试题 01.07. 旋转矩阵
'''

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 转置矩阵
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 翻转每一行
        for i in range(n):
            matrix[i] = matrix[i][::-1]