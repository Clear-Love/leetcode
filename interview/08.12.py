'''
Author: lmio 2091319361@qq.com
Date: 2023-08-09 15:36:11
LastEditors: lmio 2091319361@qq.com
Description: 面试题 08.12. 八皇后
'''

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = []
        # 可选择的列
        col = set(list(range(n)))
        # 正斜线
        pos = set(list(range(2 * n)))
        # 反斜线
        anti = set(list(range(1 - n, n)))
        def dfs(i):
            nonlocal res
            if i == n:
                res.append(path.copy())
                return
            for j in range(n):
                if j in col:
                    if i - j in anti and i + j in pos:
                        col.discard(j)
                        anti.discard(i - j)
                        pos.discard(i + j)
                        path.append('.'*(j) + 'Q' + '.'*(n-j-1))
                        dfs(i + 1)
                        path.pop()
                        col.add(j)
                        anti.add(i - j)
                        pos.add(i + j)
            return
        dfs(0)
        return res