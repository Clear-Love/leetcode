'''
Author: lmio 2091319361@qq.com
Date: 2023-07-10 14:49:55
LastEditors: lmio 2091319361@qq.com
Description: 102. 二叉树的层序遍历
'''
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            temp = []
            ans = []
            while stack:
                node = stack[0]
                stack = stack[1:]
                if not node:
                    continue
                ans.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(ans)
            stack = temp
        return res