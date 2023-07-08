'''
Author: lmio 2091319361@qq.com
Date: 2023-07-08 21:56:51
LastEditors: lmio 2091319361@qq.com
Description: 112. 路径总和
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    def pathSum(node: TreeNode, sum) -> bool:
        if not node:
            return False
        sum += node.val
        if not node.left and not node.right:
            return sum == targetSum
        return pathSum(node.left, sum) or pathSum(node.right, sum)
    return root != None and pathSum(root, 0)