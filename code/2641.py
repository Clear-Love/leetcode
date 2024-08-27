'''
Author: lmio 2091319361@qq.com
Date: 2024-03-18 20:21:53
LastEditors: lmio 2091319361@qq.com
Description: 2641. 二叉树的堂兄弟节点 II
'''

from typing import Optional

from utils.node import TreeNode


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        treeSum = []
        q = [root]
        while q:
            tmp = []
            s = 0
            while q:
                node = q.pop()
                s += node.val
                if node.left:
                    tmp.append(node.left)
                if node. right:
                    tmp.append(node.right)
            treeSum.append(s)
            q = tmp
        q = [root]
        root.val = 0
        i = 1
        while q:
            tmp = []
            while q:
                node = q.pop()
                s = 0
                l = node.left.val if node.left else 0
                r = node.right.val if node.right else 0
                if node.left:
                    node.left.val = treeSum[i]-l-r
                    tmp.append(node.left)
                if node.right:
                    node.right.val = treeSum[i]-l-r
                    tmp.append(node.right)
            i += 1
            q = tmp
        return root
