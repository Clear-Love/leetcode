'''
Author: lmio 2091319361@qq.com
Date: 2024-05-21 15:56:43
LastEditors: lmio 2091319361@qq.com
Description: 2836. 在传球游戏中最大化函数值
'''

from typing import List
    
class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        m = k.bit_length()-1
        # f[x][i] 表示编号为x的玩家传球2^i次后传给了谁
        f = [[p]+[-1]*m for p in receiver]
        # sc[x][i] 表示编号为x的玩家传球2^i次后的得分
        sc = [[p]+[0]*m for p in receiver]
        for i in range(m):
            for x in range(n):
                p = f[x][i]
                f[x][i+1] = f[p][i]
                sc[x][i+1] = sc[p][i]+sc[x][i]
        res = 0
        for i in range(n):
            x = c = i
            for j in range(m+1):
                if (k >> j) & 1:
                    c += sc[x][j]
                    x = f[x][j]
            res = max(res, c)
        return res