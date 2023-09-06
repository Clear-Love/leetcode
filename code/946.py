'''
Author: lmio 2091319361@qq.com
Date: 2023-09-04 10:07:25
LastEditors: lmio 2091319361@qq.com
Description: 946. 验证栈序列
'''

from collections import deque
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        poppe = deque(popped)
        pushe = deque(pushed)
        while pushe:
            while pushe and pushe[0] != poppe[0]:
                stack.append(pushe.popleft())
            while poppe and pushe and poppe[0] == pushe[0]:
                poppe.popleft()
                pushe.popleft()
            while stack and poppe and stack[-1] == poppe[0]:
                stack.pop()
                poppe.popleft()
        if poppe:
            return False
        return True