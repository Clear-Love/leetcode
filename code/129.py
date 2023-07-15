'''
Author: lmio 2091319361@qq.com
Date: 2023-07-08 22:29:46
LastEditors: lmio 2091319361@qq.com
Description: 129. 求根节点到叶节点数字之和
'''

from typing import Optional

from utils.node import TreeNode

def sumNumbers(root: Optional[TreeNode]) -> int:
    def sumNum(node: TreeNode, sum) -> int:
        if not node:
            return 0
        sum = sum*10 + node.val
        if not node.left and not node.right:
            return sum
        return sumNum(node.left, sum) + sumNum(node.right, sum)
    return sumNum(root, 0)