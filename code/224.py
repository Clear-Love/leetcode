'''
Author: lmio 2091319361@qq.com
Date: 2023-07-07 14:19:15
LastEditors: lmio 2091319361@qq.com
Description: 224. 基本计算器
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

def calculate(s: str) -> int:
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '(': 0,
        ')': 0
    }

    stack = []
    rpn = [0]
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
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                rpn.append(stack.pop())
            stack.pop()
        else:
            if i > 0 and tokens[i-1] == '(':
                rpn.append(0)
            while stack and precedence[token] <= precedence.get(stack[-1], 0):
                rpn.append(stack.pop())
            stack.append(token)
        i += 1
    while stack:
        rpn.append(stack.pop())
    return evalRPN(rpn)

print(calculate("1-(     -2)"))