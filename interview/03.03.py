'''
Author: lmio 2091319361@qq.com
Date: 2023-08-04 16:10:11
LastEditors: lmio 2091319361@qq.com
Description: 面试题 03.03. 堆盘子
'''

class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack and len(self.stack[-1]) < self.cap:
            self.stack[-1].append(val)
        elif self.cap:
            self.stack.append([val])
            

    def pop(self) -> int:
        res = -1
        if self.stack and self.stack[-1]:
            res = self.stack[-1].pop()
            if not self.stack[-1]:
                self.stack.pop()
        return res

    def popAt(self, index: int) -> int:
        res = -1
        if 0 <= index < len(self.stack):
            res = self.stack[index].pop()
            if not self.stack[index]:
                self.stack.pop(index)
        return res