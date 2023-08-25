'''
Author: lmio 2091319361@qq.com
Date: 2023-08-20 15:52:26
LastEditors: lmio 2091319361@qq.com
Description: 2236. 判断根结点是否等于子结点之和
'''

from typing import Optional

from utils.node import TreeNode


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.left.val + root.right.val == root.val