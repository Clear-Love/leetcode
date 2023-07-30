'''
Author: lmio 2091319361@qq.com
Date: 2023-07-30 15:51:34
LastEditors: lmio 2091319361@qq.com
Description: 2336. 无限集中的最小数字
'''

class SmallestInfiniteSet:

    def __init__(self):
        self.minVal = 1
        self.rmVal = set()

    def popSmallest(self) -> int:
        self.rmVal.add(self.minVal)
        tmp = self.minVal
        val = self.minVal + 1
        while val in self.rmVal:
            val += 1
        self.minVal = val
        return tmp

    def addBack(self, num: int) -> None:
        self.rmVal.discard(num)
        self.minVal = min(self.minVal, num)