'''
Author: lmio 2091319361@qq.com
Date: 2024-04-03 23:27:48
LastEditors: lmio 2091319361@qq.com
Description: 
'''

_ = int(input())
ws = list(map(int, input().split(" ")))
m = set()
for w in ws:
    for v in list(m):
        m.add(v+w)
        m.add(abs(v-w))
    m.add(w)
print(len(m))