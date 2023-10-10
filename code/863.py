'''
Author: lmio 2091319361@qq.com
Date: 2023-10-06 23:38:56
LastEditors: lmio 2091319361@qq.com
Description: 863. 二叉树中所有距离为 K 的结点
'''

from typing import List
from utils.node import TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        pre = {}
        def helper(root, parent=None):
            if not root:
                return 
            pre[root] = parent
            helper(root.left, root)
            helper(root.right, root)
        helper(root)
        res = []
        def getDepth(node, parent=None, gap=0):
            if not node:
                return
            if gap == k:
                res.append(node.val)
                return
            if node.left != parent:
                getDepth(node.left, node, gap + 1)
            if node.right != parent:
                getDepth(node.right, node, gap + 1)
            if pre[node] != parent:
                getDepth(pre[root], node, gap + 1)
        getDepth(target)
        return res