'''
Author: lmio 2091319361@qq.com
Date: 2023-08-04 00:07:42
LastEditors: lmio 2091319361@qq.com
Description: 657. 机器人能否返回原点
'''
from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnts = Counter(moves)
        return cnts['U'] == cnts['D'] and cnts['L'] == cnts['R']