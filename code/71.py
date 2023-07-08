'''
Author: lmio 2091319361@qq.com
Date: 2023-07-07 13:33:10
LastEditors: lmio 2091319361@qq.com
Description: 71. 简化路径
'''

def simplifyPath(path: str) -> str:
    path = path.split('/')
    stack = []
    for s in path:
        if s == '' or s == '.':
            continue
        elif s == '..':
            stack = stack[:-1]
        else:
            stack.append(s)
    return '/' + '/'.join(stack)