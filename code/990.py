'''
Author: lmio 2091319361@qq.com
Date: 2023-10-17 20:20:20
LastEditors: lmio 2091319361@qq.com
Description: 990. 等式方程的可满足性
'''

from typing import List

from utils.unionFind import unionFind




class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        eq = unionFind()
        uneq = []
        for equation in equations:
            a, b = equation[0], equation[-1]
            if equation[1] == '=':
                eq.union(a, b)
            else:
                uneq.append(equation)
        for equation in uneq:
            a, b = equation[0], equation[-1]
            if eq.find(a) == eq.find(b):
                return False
        return True