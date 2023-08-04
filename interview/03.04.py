'''
Author: lmio 2091319361@qq.com
Date: 2023-08-04 17:06:18
LastEditors: lmio 2091319361@qq.com
Description: 面试题 03.04. 化栈为队
'''

class MyQueue:

    def __init__(self):
        self.stack = []
        self.queue = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        stack = self.stack
        if not self.queue:
            while stack:
                self.queue.append(stack.pop())
        if self.queue:
            return self.queue.pop()
        return -1

    def peek(self) -> int:
        stack = self.stack
        if not self.queue:
            while stack:
                self.queue.append(stack.pop())
        if self.queue:
            return self.queue[-1]
        return -1

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.queue) == 0