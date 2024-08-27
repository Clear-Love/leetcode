'''
Author: lmio 2091319361@qq.com
Date: 2024-05-31 15:16:13
LastEditors: lmio 2091319361@qq.com
Description: 斐波那契与7
'''
cycle = [1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1, 0]
N = 202202011200

c = cycle.count(7)
n = len(cycle)

#每 n 项 出现c个7

print((N//n)*c + cycle[:N%n].count(7))