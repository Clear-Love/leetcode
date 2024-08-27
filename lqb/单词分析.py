'''
Author: lmio 2091319361@qq.com
Date: 2024-04-12 21:23:12
LastEditors: lmio 2091319361@qq.com
Description: 单词分析
'''

from typing import Counter


cnts = Counter(input())
w, cnt = 0, 0
for ch, c in cnts.items():
    if c > cnt or (c == cnt and ch < w):
        cnt = c
        w = ch
print(w)
print(cnt)