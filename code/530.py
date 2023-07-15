'''
Author: lmio 2091319361@qq.com
Date: 2023-07-10 15:35:51
LastEditors: lmio 2091319361@qq.com
Description: 530. 二叉搜索树的最小绝对差
'''

from typing import Optional

from utils.node import TreeNode

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