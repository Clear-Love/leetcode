'''
Author: lmio 2091319361@qq.com
Date: 2023-07-07 13:20:52
LastEditors: lmio 2091319361@qq.com
Description: 20. 有效的括号
'''

def isValid(s: str) -> bool:
    stack = []
    for ch in s:
        if len(stack) > 0 and stack[-1] == ch:
            stack.pop()
        elif ch == '(':
            stack.append(')')
        elif ch == '[':
            stack.append(']')
        elif ch == '{':
            stack.append('}')
        else:
            return False
    return len(stack) == 0
