'''
Author: lmio 2091319361@qq.com
Date: 2023-08-04 18:02:34
LastEditors: lmio 2091319361@qq.com
Description: 面试题 03.05. 栈排序
'''
class SortedStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        stack = self.stack
        tmp = []
        while stack and val > stack[-1]:
            tmp.append(stack.pop())
        stack.append(val)
        while tmp:
            stack.append(tmp.pop())

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()
        return -1


    def peek(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.stack) == 0