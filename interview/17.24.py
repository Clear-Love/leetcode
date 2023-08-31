'''
Author: lmio 2091319361@qq.com
Date: 2023-08-29 22:22:56
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.24. 最大子矩阵
'''

from typing import List


class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        preSum = [[0 for _ in range(m+1)] for _ in range(n+1)]
        maxVal = float('-inf')
        res = []
        # 二维前缀和
        for i in range(1, n+1):
            for j in range(1, m+1):
                preSum[i][j] = matrix[i-1][j-1] + preSum[i][j-1] + preSum[i-1][j] - preSum[i-1][j-1]
        for up in range(n):
            for down in range(up, n):
                left = 0
                for right in range(m):
                    s = preSum[down+1][right+1] - preSum[down+1][left] - preSum[up][right+1] + preSum[up][left]
                    if s > maxVal:
                        maxVal = s
                        res = [up, left, down, right]
                    if s < 0:
                        left = right+1
        return res