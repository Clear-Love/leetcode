'''
Author: lmio 2091319361@qq.com
Date: 2023-07-10 15:35:51
LastEditors: lmio 2091319361@qq.com
Description: 530. 二叉搜索树的最小绝对差
'''

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans, pre = float('inf'), float('-inf')
        def dfs(node: TreeNode):
            nonlocal ans, pre
            if not node:
                return
            dfs(node.left)
            if node.val - pre < ans:
                ans = node.val - pre
            pre = node.val
            dfs(node.right)
        dfs(root)
        return ans