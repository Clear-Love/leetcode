'''
Author: lmio 2091319361@qq.com
Date: 2023-08-09 14:45:15
LastEditors: lmio 2091319361@qq.com
Description: 面试题 08.09. 括号
'''

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lNum = n
        rNum = n
        res = []
        path = []
        def dfs():
            nonlocal lNum, rNum
            if len(path) == 2*n:
                res.append(''.join(path))
            if lNum > 0:
                path.append('(')
                lNum -= 1
                dfs()
                lNum += 1
                path.pop()
            if rNum > lNum:
                path.append(')')
                rNum -= 1
                dfs()
                rNum += 1
                path.pop()
        dfs()
        return res