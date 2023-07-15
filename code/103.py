'''
Author: lmio 2091319361@qq.com
Date: 2023-07-10 15:04:28
LastEditors: lmio 2091319361@qq.com
Description: 103. 二叉树的锯齿形层序遍历
'''

from typing import List, Optional
from collections import deque

from utils.node import TreeNode
        
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        res = []
        lTr = True
        while stack:
            temp = []
            ans = deque()
            while stack:
                node = stack[0]
                stack = stack[1:]
                if lTr:
                    ans.append(node.val)
                else:
                    ans.appendleft(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(list(ans))
            lTr = not lTr
            stack = temp
        return res