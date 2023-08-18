'''
Author: lmio 2091319361@qq.com
Date: 2023-08-17 22:59:49
LastEditors: lmio 2091319361@qq.com
Description: 面试题 16.26. 计算器
'''

from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        def evalRPN(tokens: List[str]) -> int:
            stack =[]
            for token in tokens:
                if token == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b + a)
                elif token == '-':
                    a = stack.pop()
                    b = 0 if not stack else stack.pop()
                    stack.append(b - a)
                elif token == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b * a)
                elif token == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))
                else:
                    stack.append(int(token))
            return stack[-1]
        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        }
        # 转换为波兰表达式
        stack = []
        rpn = [0]
        # 去除空格
        s = s.replace(" ", "")
        tokens = list(s)
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.isdigit():
                j = i + 1
                while j < len(tokens) and tokens[j].isdigit():
                    token += tokens[j]
                    j += 1
                i = j-1
                rpn.append(token)
            else:
                # 操作符 栈中的操作符保保持从小到大
                while stack and precedence[token] <= precedence.get(stack[-1], 0):
                    rpn.append(stack.pop())
                stack.append(token)
            i += 1
        while stack:
            rpn.append(stack.pop())
        return evalRPN(rpn)