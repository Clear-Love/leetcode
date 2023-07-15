'''
Author: lmio 2091319361@qq.com
Date: 2023-07-14 20:25:07
LastEditors: lmio 2091319361@qq.com
Description: 427. 建立四叉树
'''
from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r0,r1,c0,c1):
            for i in range(r0,r1):
                for j in range(c0,c1):
                    # 不是叶子结点
                    if grid[i][j]!=grid[r0][c0]:
                        return Node(True,False,
                                    dfs(r0,(r0+r1)//2,c0,(c0+c1)//2),
                                    dfs(r0,(r0+r1)//2,(c0+c1)//2,c1),
                                    dfs((r0+r1)//2,r1,c0,(c0+c1)//2),
                                    dfs((r0+r1)//2,r1,(c0+c1)//2,c1))
            return Node(grid[r0][c0],True)
        return dfs(0,len(grid),0,len(grid))