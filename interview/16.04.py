'''
Author: lmio 2091319361@qq.com
Date: 2023-08-11 16:05:26
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.04. 井字游戏
'''

import re
from typing import List


class Solution:
    def tictactoe(self, board: List[str]) -> str:
        n = len(board)
        def canWin(char: str) -> bool:
            # 正对角线
            i = 0
            while i < n:
                if board[i][i] != char:
                    break
                i += 1
            if i == n:
                return True
            i = 0
            while i < n:
                if board[i][n-1-i] != char:
                    break
                i += 1
            if i == n:
                return True
            # 行列
            for i in range(n):
                if all(char == ch for ch in board[i]):
                    return True
            for j in range(n):
                if all(board[i][j] == char for i in range(n)):
                    return True
            return False
        if canWin('X'):
            return 'X'
        if canWin('O'):
            return 'O'
        for i in range(n):
            if ' ' in board[i]:
                return 'Pending'
        return 'Draw'