'''
Author: lmio 2091319361@qq.com
Date: 2023-08-08 16:43:49
LastEditors: lmio 2091319361@qq.com
Description: 面试题 08.07. 无重复字符串的排列组合
'''

from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        n = len(S)
        res = []
        path = []
        visited = set()
        def dfs():
            if len(path) == n:
                res.append(''.join(path))
                return
            for ch in S:
                if ch not in visited:
                    visited.add(ch)
                    path.append(ch)
                    dfs()
                    path.pop()
                    visited.remove(ch)
        dfs()
        return res