'''
Author: lmio 2091319361@qq.com
Date: 2023-08-27 10:38:48
LastEditors: lmio 2091319361@qq.com
Description: 8015. 距离原点最远的点
'''

from collections import Counter


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnts = Counter(moves)
        if cnts.get('R', 0) > cnts.get('L', 0):
            return cnts.get('R', 0) + cnts.get('_', 0) - cnts.get('L', 0)
        else:
            return cnts.get('L', 0) + cnts.get('_', 0) - cnts.get('R', 0)