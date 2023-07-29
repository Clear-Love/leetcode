'''
Author: lmio 2091319361@qq.com
Date: 2023-07-29 15:30:12
LastEditors: lmio 2091319361@qq.com
Description: 1448. 统计二叉树中好节点的数目
'''
from utils.node import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxVal = float('-inf')
        res = 0
        def dfs(node: TreeNode):
            nonlocal maxVal, res
            if not node:
                return
            maxVal = max(maxVal, node.val)
            tmp = maxVal
            if maxVal == node.val:
                res += 1
            dfs(node.left)
            maxVal = tmp
            dfs(node.right)
        dfs(root)
        return res