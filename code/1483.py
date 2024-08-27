'''
Author: lmio 2091319361@qq.com
Date: 2024-05-21 15:14:15
LastEditors: lmio 2091319361@qq.com
Description: 1483. 树节点的第 K 个祖先
'''

from typing import List


class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        m = n.bit_length()-1
        pa = [[p]+[-1]*m for p in parent]
        # 动态规划
        for i in range(m):
            for x in range(n):
                if (p := pa[x][i]) != -1: 
                    pa[x][i + 1] = pa[p][i]
        self.pa = pa

    def getKthAncestor(self, node: int, k: int) -> int:
        while k and node != -1:  # 不断去掉 k 的最低位的 1
            lb = k & -k
            node = self.pa[node][lb.bit_length()-1]
            k ^= lb
        return node