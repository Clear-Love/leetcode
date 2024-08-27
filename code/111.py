'''
Author: lmio 2091319361@qq.com
Date: 2024-05-07 20:23:28
LastEditors: lmio 2091319361@qq.com
Description: 111. 二叉树的最小深度
'''

from collections import deque
from typing import Optional

from utils.node import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        k = 1
        while q:
            tmp = deque()
            while q:
                node = q.popleft()
                if not node.left and not node.right:
                    return k
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            q = tmp
            k += 1
        return -1