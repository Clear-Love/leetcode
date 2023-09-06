'''
Author: lmio 2091319361@qq.com
Date: 2023-09-01 15:10:43
LastEditors: lmio 2091319361@qq.com
Description: 144. 二叉树的前序遍历
'''
from typing import Optional

from utils.node import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val]
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))
        return res