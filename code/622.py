'''
Author: lmio 2091319361@qq.com
Date: 2023-09-06 09:32:05
LastEditors: lmio 2091319361@qq.com
Description: 622. 设计循环队列
'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = 0
        self.queue = [0]*k
        self.cap = k
        self.len = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        pos = (self.head + self.len)%self.cap
        self.queue[pos] = value
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if self.len == 0:
            return False
        self.head = (self.head+1)%self.cap
        self.len -= 1
        return True

    def Front(self) -> int:
        if self.len == 0:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.len == 0:
            return -1
        return self.queue[(self.head+self.len-1)%self.cap]

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.cap