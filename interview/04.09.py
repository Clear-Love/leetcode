'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 15:55:50
LastEditors: lmio 2091319361@qq.com
Description: 面试题 04.09. 二叉搜索树序列
'''

from typing import List
from utils.node import TreeNode


class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        res = []
        ans = [root.val]
        queue = []
        def braceback(node: TreeNode):
            nonlocal queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if not queue:
                res.append(ans.copy())
                return
            for i in range(len(queue)):
                v = queue[i]
                tmp = queue
                queue = queue[:i] + queue[i+1:]
                ans.append(v.val)
                braceback(v)
                ans.pop()
                queue = tmp
        braceback(root)
        return res