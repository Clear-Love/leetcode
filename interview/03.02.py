'''
Author: lmio 2091319361@qq.com
Date: 2023-08-04 16:04:22
LastEditors: lmio 2091319361@qq.com
Description: 面试题 03.02. 栈的最小值
'''

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minStack or self.minStack[-1] >= x:
            self.minStack.append(x)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if self.minStack and self.minStack[-1] == val:
                self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]