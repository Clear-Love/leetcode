'''
Author: lmio 2091319361@qq.com
Date: 2023-08-26 23:30:12
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.20. 连续中值
'''

import heapq


class MedianFinder:

    def __init__(self):
        self.pre = []
        self.next = []
        self.size = 0

    def addNum(self, num: int) -> None:
        if not self.pre or num < -self.pre[0]:
            heapq.heappush(self.pre, -num)
        else:
            heapq.heappush(self.next, num)
        while len(self.pre) > len(self.next) + 1:
            heapq.heappush(self.next, -heapq.heappop(self.pre))
        while len(self.pre) < len(self.next):
            heapq.heappush(self.pre, -heapq.heappop(self.next))
        self.size += 1

    def findMedian(self) -> float:
        if self.size & 1:
            return -self.pre[0]
        else:
            return (self.next[0] - self.pre[0])/2