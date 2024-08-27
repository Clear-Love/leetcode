'''
Author: lmio 2091319361@qq.com
Date: 2024-05-31 19:55:18
LastEditors: lmio 2091319361@qq.com
Description: 替换字符
'''

s = list(input())
n = int(input())

for i in range(n):
    l, r, x, y = input().split(" ")
    l = int(l)
    r = int(r)
    for k in range(l-1, r):
        if s[k] == x:
            s[k] = y
s = ''.join(s)
print(s)