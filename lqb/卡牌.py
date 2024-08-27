'''
Author: lmio 2091319361@qq.com
Date: 2024-04-06 16:58:26
LastEditors: lmio 2091319361@qq.com
Description: 卡牌
'''

import heapq


n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

q = [(c, i) for i, c in enumerate(a)]
heapq.heapify(q)
while m:
    c, i = heapq.heappop(q)
    if b[i] == 0:
        break
    b[i] -= 1
    # 画一张
    heapq.heappush(q, (c+1, i))
    m -= 1
print(q[0][0])