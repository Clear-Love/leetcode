'''
Author: lmio 2091319361@qq.com
Date: 2023-08-11 15:56:38
LastEditors: lmio 2091319361@qq.com
Description: 1572. 矩阵对角线元素的和
'''

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = 0
        for i in range(n):
            res += mat[i][i] + mat[i][n-1-i]
        if n&1:
            res -= mat[n//2][n//2]
        return res