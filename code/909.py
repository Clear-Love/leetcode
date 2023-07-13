'''
Author: lmio 2091319361@qq.com
Date: 2023-07-11 17:53:37
LastEditors: lmio 2091319361@qq.com
Description: 
'''
from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # x -> pos
        def transform(idx):
            i = n - 1 - (idx - 1) // n
            j = idx - 1 - (n - 1 - i) * n if i % 2 != n % 2 else (n - i) * n - idx
            return i, j

        queue = deque([(1, 0)])
        visited = {1}
        while queue:
            x, step = queue.popleft()
            if x == n * n:
                return step
            # 跳跃到没有蛇或者梯子的地方要跳尽可能远
            already = False
            for dx in range(6, 0, -1):
                next = x + dx
                if next > n * n:
                    continue
                if next not in visited:
                    i, j = transform(next)
                    visited.add(next)
                    if board[i][j] != -1:
                        # 遇到梯子
                        queue.append((board[i][j], step + 1))
                    elif not already:
                        # 没遇到梯子，选择跳得最远的
                        queue.append((next, step + 1))
                        already = True
        return -1
