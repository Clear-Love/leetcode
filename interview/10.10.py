'''
Author: lmio 2091319361@qq.com
Date: 2023-08-10 00:01:04
LastEditors: lmio 2091319361@qq.com
Description: 面试题 10.10. 数字流的秩
'''

import bisect


class StreamRank:

    def __init__(self):
        self.arr = []

    def track(self, x: int) -> None:
        bisect.insort(self.arr, x)

    def getRankOfNumber(self, x: int) -> int:
        return bisect.bisect(self.arr, x)