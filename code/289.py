'''
Author: lmio 2091319361@qq.com
Date: 2023-07-05 20:01:46
LastEditors: lmio 2091319361@qq.com
Description: 289. 生命游戏
'''

import copy
from typing import List


def gameOfLife(self, board: List[List[int]]) -> None:
    n, m = len(board), len(board[0])
    modify = {}
    d = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    def around_liveCnt(x: int, y: int) -> int:
        live_cnt = 0
        for dx, dy in d:
            cur_x = x + dx
            cur_y = y + dy
            if cur_x >= 0 and cur_x < n and cur_y >= 0 and cur_y < m and board[cur_x][cur_y] == 1:
                live_cnt += 1
        return live_cnt
    for i in range(len(board)):
        for j in range(len(board[i])):
            liveCnt = around_liveCnt(i, j)
            if board[i][j] == 1:
                if liveCnt < 2:
                    modify[(i, j)] = 0
                elif liveCnt > 3:
                    modify[(i, j)] = 0
            else:
                if liveCnt == 3:
                    modify[(i, j)] = 1
    for pos, val in modify.items():
        board[pos[0]][pos[1]] = val