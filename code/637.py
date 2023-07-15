'''
Author: lmio 2091319361@qq.com
Date: 2023-07-10 13:53:49
LastEditors: lmio 2091319361@qq.com
Description: 637. 二叉树的层平均值
'''

from collections import namedtuple
from typing import Optional, List

from utils.node import TreeNode

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack = [root]
        res = []
        while stack:
            temp = []
            sum = 0
            cnt = 0
            while stack:
                node = stack.pop()
                if not node:
                    continue
                sum += node.val
                cnt += 1
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(sum/cnt)
            stack = temp
        return res
