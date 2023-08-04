'''
Author: lmio 2091319361@qq.com
Date: 2023-08-04 15:45:53
LastEditors: lmio 2091319361@qq.com
Description: 面试题 03.01. 三合一
'''

class TripleInOne:
    def __init__(self, stackSize: int):
        self.stackSize = stackSize
        self.arr = [[] for _ in range(3)]

    def push(self, stackNum: int, value: int) -> None:
        if len(self.arr[stackNum]) < self.stackSize:
            self.arr[stackNum].append(value)

    def pop(self, stackNum: int) -> int:
        if self.arr[stackNum]:
            return self.arr[stackNum].pop()
        else:
            return -1

    def peek(self, stackNum: int) -> int:
        if self.arr[stackNum]:
            return self.arr[stackNum][-1]
        else:
            return -1

    def isEmpty(self, stackNum: int) -> bool:
        return len(self.arr[stackNum]) == 0