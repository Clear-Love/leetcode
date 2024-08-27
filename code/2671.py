'''
Author: lmio 2091319361@qq.com
Date: 2024-03-21 13:35:20
LastEditors: lmio 2091319361@qq.com
Description: 2671. 频率跟踪器
'''

from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        self.cnts = defaultdict(int)
        self.freq = defaultdict(set)

    def add(self, number: int) -> None:
        self.cnts[number] += 1
        c = self.cnts[number]
        self.freq[c-1].discard(number)
        self.freq[c].add(number)

    def deleteOne(self, number: int) -> None:
        if number in self.cnts:
            c = self.cnts[number]
            self.cnts[number] -= 1
            self.freq[c].remove(number)
            if self.cnts[number] == 0:
                del self.cnts[number]
            else:
                self.freq[c-1].add(number)


    def hasFrequency(self, frequency: int) -> bool:
        return len(self.freq[frequency]) > 0