'''
Author: lmio 2091319361@qq.com
Date: 2024-03-19 16:54:32
LastEditors: lmio 2091319361@qq.com
Description: 987. 二叉树的垂序遍历
'''


from collections import defaultdict
from typing import List, Optional
from utils.node import TreeNode


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        g = defaultdict(list)
        q = [(root, 0)]
        while q:
            tmp = []
            t = defaultdict(list)
            while q:
                node, col = q.pop()
                t[col].append(node.val)
                if node.left:
                    tmp.append((node.left, col-1))
                if node.right:
                    tmp.append((node.right, col+1))
            for col, lst in t.items():
                for v in sorted(lst):
                    g[col].append(v)
            q = tmp
        return [g[x] for x in sorted(g.keys())]