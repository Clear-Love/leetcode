'''
Author: lmio 2091319361@qq.com
Date: 2023-07-07 13:46:13
LastEditors: lmio 2091319361@qq.com
Description: 155. 最小栈
'''

class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        val = self.stack.pop()
        if self.min[-1] == val:
            self.min.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.min[-1]