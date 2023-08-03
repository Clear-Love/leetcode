'''
Author: lmio 2091319361@qq.com
Date: 2023-08-03 09:07:49
LastEditors: lmio 2091319361@qq.com
Description: 面试题 01.05. 一次编辑
'''

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        n, m = len(first), len(second)
        first, second = list(first), list(second)
        if abs(n - m) > 1:
            return False
        for i in range(min(n, m)):
            if first[i] != second[i]:
                return first[i+1:] == second[i+1:] or \
                    first[i+1:] == second[i:] or \
                    first[i:] == second[i+1:]
        return True