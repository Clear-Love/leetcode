from typing import List
from scipy.optimize import linear_sum_assignment
from scipy.spatial.distance import cdist

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        fr = []
        to = []
        for i in range(n):
            for j in range(m):
                v = grid[i][j]
                if v > 1:
                    fr.extend([(i, j)]*(v-1))
                elif v == 0:
                    to.append((i, j))
        matrix = cdist(fr, to, metric='cityblock')
        row, col = linear_sum_assignment(matrix)
        return int(matrix[row, col].sum())