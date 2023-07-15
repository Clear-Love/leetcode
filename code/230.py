'''
Author: lmio 2091319361@qq.com
Date: 2023-07-10 16:50:35
LastEditors: lmio 2091319361@qq.com
Description: 230. 二叉搜索树中第K小的元素
'''

from typing import Optional

from utils.node import TreeNode
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans, index = float('inf'), 0
        def dfs(node: TreeNode):
            nonlocal ans, index
            if not node:
                return
            dfs(node.left)
            index += 1
            print(node.val, index)
            if index == k:
                ans = node.val
                return
            if index > k:
                return
            dfs(node.right)
        dfs(root)
        return ans