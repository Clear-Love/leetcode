'''
Author: lmio 2091319361@qq.com
Date: 2024-04-03 16:11:38
LastEditors: lmio 2091319361@qq.com
Description: 括号序列
'''

from collections import defaultdict
import math


s = input()
cnts = defaultdict(int)
for w in s:
    cnts[w] += 1
n = max(cnts['('], cnts[')'])
MOD = 10**9+7
print(math.comb(2*n, n)//(n+1)%MOD)