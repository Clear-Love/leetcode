'''
Author: lmio 2091319361@qq.com
Date: 2023-07-11 16:13:54
LastEditors: lmio 2091319361@qq.com
Description: 并查集
'''
class UnionFind:
    def __init__(self):
        self.parent = {}  # 初始化每个元素的父节点为自身
        self.rank = {}  # 用于记录每个集合的秩（深度）

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩，将x的父节点直接设为根节点
        return self.parent[x]

    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        # 找rank大的作为根
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

    def is_connected(self,x,y):
        # 判断两节点是否相连
        return self.find(x) == self.find(y)
    
    def add(self,x):
        # 添加新节点
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0