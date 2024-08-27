'''
Author: lmio 2091319361@qq.com
Date: 2024-03-14 16:43:22
LastEditors: lmio 2091319361@qq.com
Description: 从数据流中查找中位数
'''


import heapq


class MedianFinder:
    def __init__(self):
        # 使用两个堆来存储数据流中的元素
        self.small = []  # 存储较小的一半元素的最大堆
        self.large = []  # 存储较大的一半元素的最小堆

    def addNum(self, num: int) -> None:
        # 将新的元素添加到合适的堆中
        heapq.heappush(self.small, -num)  # 使用负数来实现最大堆
        # 将最大堆中的最大元素转移到最小堆中
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # 调整堆的大小，使得两个堆的大小差距不超过 1
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # 根据两个堆的大小来计算中位数
        if len(self.large) == len(self.small):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return -self.small[0]
