'''
Author: lmio 2091319361@qq.com
Date: 2023-07-07 13:58:16
LastEditors: lmio 2091319361@qq.com
Description: 150. 逆波兰表达式求值
'''

from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack =[]
    for token in tokens:
        if token == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)
        elif token == '-':
            a = stack.pop()
            b = stack.pop()
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