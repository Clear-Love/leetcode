'''
Author: lmio 2091319361@qq.com
Date: 2023-07-16 17:38:50
LastEditors: lmio 2091319361@qq.com
Description: 834. 树中距离之和
'''
from collections import defaultdict
from typing import List


from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # 构建树的邻接表表示
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # 初始化结果数组
        res = [0] * n
        # 子数组节点数
        subtree_size = [0] * n
        def dfs1(node, parent):
            subtree_size[node] = 1
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                dfs1(neighbor, node)
                subtree_size[node] += subtree_size[neighbor]
                res[node] += res[neighbor] + subtree_size[neighbor]
        def dfs2(node, parent):
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                # 从父节点距离和到当前节点距离和
                # 子树内部节点：与当前节点距离 = 与父节点距离 - 1
                # 子树外部节点：与当前节点距离 = 与父节点距离 + 1
                # 当前距离和： 父距离和 -（内部节点数）+（外部节点数）
                res[neighbor] = res[node] - subtree_size[neighbor] + (n - subtree_size[neighbor])
                dfs2(neighbor, node)
        # 树形dp初始化，推算出根节点距离和（无向、连通树任意节点都可以当作根节点）
        dfs1(0, -1)
        # 动态规划
        dfs2(0, -1)
        return res