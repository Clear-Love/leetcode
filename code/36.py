'''
Author: lmio 2091319361@qq.com
Date: 2023-07-05 16:53:17
LastEditors: lmio 2091319361@qq.com
Description: 36. 有效的数独
'''

from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    n, m = len(board[0]), len(board)
    row = [set() for _ in range(n)]
    col = [set() for _ in range(m)]
    block = [[set() for _ in range(n//3)] for _ in range(m//3)]
    for i in range(n):
        for j in range(m):
            ch = board[i][j]
            if ch == '.':
                continue
            if ch in row[j]:
                return False
            else:
                row[j].add(ch)
            if ch in col[i]:
                return False
            else:
                col[i].add(ch)
            r, c = i//3, j//3
            if ch in block[r][c]:
                return False
            else:
                block[r][c].add(ch)
    return True