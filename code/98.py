'''
Author: lmio 2091319361@qq.com
Date: 2023-07-10 17:00:35
LastEditors: lmio 2091319361@qq.com
Description: 98. 验证二叉搜索树
'''

from typing import Optional
from utils.node import TreeNode

        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans, pre = True, float('-inf')
        def dfs(node: TreeNode):
            nonlocal ans, pre
            if not node:
                return
            dfs(node.left)
            if node.val <= pre:
                ans = False
            pre = node.val
            dfs(node.right)
        return ans