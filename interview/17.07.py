'''
Author: lmio 2091319361@qq.com
Date: 2023-08-19 15:56:22
LastEditors: lmio 2091319361@qq.com
Description: 面试题 17.07. 婴儿名字
'''
from collections import defaultdict
from typing import List


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        parent, cnts = {}, {}
        for s in names:
            name, cnt = s.split("(")
            parent[name], cnts[name] = name, int(cnt[:-1])
        # 并查集查找同类根
        def find(x):
            if parent[x] != x: 
                parent[x] = find(parent[x])
            return parent[x]
        for s in synonyms:
            name1, name2 = s[1:-1].split(",")
            # 不存在的话 仍然需要在f和cnt里进行增加 因为连接关系仍有用
            if name1 not in parent:
                parent[name1] = name1
                cnts[name1] = 0
            if name2 not in parent:
                parent[name2] = name2
                cnts[name2] = 0
            p1, p2 = find(name1), find(name2)
            if p1 == p2:
                # 父亲一样 那么此时什么都不做
                continue
            # 父亲不一样 需要合并 字典序小的作为父亲
            cnt = cnts[p1] + cnts[p2]
            fa = min(p1, p2)
            ch = max(p1, p2)
            parent[ch] = fa
            cnts[ch] = 0
            cnts[fa] = cnt
        res = {}
        for name, p in parent.items():
            # 根节点
            if name == p and cnts[name] != 0:
                res[name] = cnts[name]
        return [f'{name}({cnt})' for name, cnt in res.items()]