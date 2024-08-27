'''
Author: lmio 2091319361@qq.com
Date: 2024-03-13 18:55:37
LastEditors: lmio 2091319361@qq.com
Description: 225. 用队列实现栈
'''

from collections import deque


class MyStack:

    def __init__(self):
        self.queue = deque()


    def push(self, x: int) -> None:
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())
        
    def pop(self) -> int:
        return self.queue.popleft()


    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue