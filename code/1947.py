from typing import List
import numpy as np
from scipy.optimize import linear_sum_assignment


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])
        def compatibility(stuRes: List[int], menRes: List[int]) -> int:
            res = 0
            for i in range(n):
                if stuRes[i] == menRes[i]:
                    res += 1
            return res
        matrix = np.zeros((m, m))
        for i in range(m):
            for j in range(m):
                matrix[i, j] = -compatibility(students[i], mentors[j])
        row, col = linear_sum_assignment(matrix)
        return int(-matrix[row, col].sum())