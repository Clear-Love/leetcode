'''
Author: lmio 2091319361@qq.com
Date: 2024-05-31 19:22:24
LastEditors: lmio 2091319361@qq.com
Description: 点亮
'''

from collections import deque


n = int(input())

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

mat =[]

zhu = deque()

for i in range(n):
    mat.append(list(input()))
    for j in range(n):
        if mat[i][j] != '.':
            zhu.append((i,j))

