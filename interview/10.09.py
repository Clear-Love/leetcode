'''
Author: lmio 2091319361@qq.com
Date: 2023-08-09 23:34:36
LastEditors: lmio 2091319361@qq.com
Description: 面试题 10.09. 排序矩阵查找
'''

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        n, m = len(matrix), len(matrix[0])
        row = 0
        while row < n and matrix[row][0] > target:
            row += 1
        for i in range(row, n):
            left, right = 0, m-1
            while left <= right:
                mid = (left + right) >> 1
                val = matrix[i][mid]
                if val == target:
                    return True
                if val > target:
                    right = mid-1
                else:
                    left = mid+1
        return False