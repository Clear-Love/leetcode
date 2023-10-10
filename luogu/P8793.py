'''
Author: lmio 2091319361@qq.com
Date: 2023-10-01 21:42:45
LastEditors: lmio 2091319361@qq.com
Description: P8793 [蓝桥杯 2022 国 A] owo
'''

import heapq
from typing import List


n = int(input())
strs: List[str] = []
for _ in range(n):
    strs.append(input())
beginW = []
beginO = []
def countOccurrences(string, s):
    count = 0
    start = 0
    while True:
        index = string.find(s, start)
        if index == -1:
            break
        count += 1
        start = index + 1
    return count
