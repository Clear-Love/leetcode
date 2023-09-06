'''
Author: lmio 2091319361@qq.com
Date: 2023-09-06 10:50:01
LastEditors: lmio 2091319361@qq.com
Description: 301. 删除无效的括号
'''

from collections import Counter
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        lremove, rremove = 0, 0
        stack = []
        path = []
        for ch in s:
            if ch == '(':
                lremove += 1
            elif ch == ')':
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1
        def dfs(i: int):
            nonlocal lremove, rremove, path
            if i == len(s) and lremove == rremove == 0:
                if not stack:
                    res.add(''.join(path))
                return
            if lremove+rremove > len(s)-i:
                return
            if s[i] not in '()':
                path.append(s[i])
                dfs(i+1)
                path.pop()
                return
            if s[i] == '(':
                # 删除
                if lremove:
                    lremove -= 1
                    dfs(i+1)
                    lremove += 1
                # 选
                stack.append(1)
                path.append(s[i])
                dfs(i+1)
                path.pop()
                stack.pop()
            if s[i] == ')':
                # 删除
                if rremove:
                    rremove -= 1
                    dfs(i+1)
                    rremove += 1
                if not stack:
                    return
                # 选
                stack.pop()
                path.append(s[i])
                dfs(i+1)
                path.pop()
                stack.append(1)
        dfs(0)
        return list(res)