'''
Author: lmio 2091319361@qq.com
Date: 2023-09-01 17:37:01
LastEditors: lmio 2091319361@qq.com
Description: 232. 用栈实现队列
'''

class MyQueue:

    def __init__(self):
        self.put = []
        self.out = []

    def push(self, x: int) -> None:
        self.put.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        if self.out:
            return self.out.pop()
        else:
            while self.put:
                self.out.append(self.put.pop())
            return self.out.pop()

    def peek(self) -> int:
        if self.empty():
            return -1
        if self.out:
            return self.out[-1]
        else:
            while self.put:
                self.out.append(self.put.pop())
            return self.out[-1]

    def empty(self) -> bool:
        return not self.put and not self.out