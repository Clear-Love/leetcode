'''
Author: lmio 2091319361@qq.com
Date: 2023-07-14 19:12:05
LastEditors: lmio 2091319361@qq.com
Description: 52. N 皇后 II
'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        # 可选择的列
        col = set(list(range(n)))
        # 正斜线
        pos = set(list(range(2 * n)))
        # 反斜线
        anti = set(list(range(1 - n, n)))
        def dfs(i):
            nonlocal res
            if i == n:
                res += 1
                return
            for j in range(n):
                if j in col:
                    if i - j in anti and i + j in pos:
                        col.discard(j)
                        anti.discard(i - j)
                        pos.discard(i + j)
                        dfs(i + 1)
                        col.add(j)
                        anti.add(i - j)
                        pos.add(i + j)
            return
        dfs(0)
        return res