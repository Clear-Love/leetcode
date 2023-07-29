'''
Author: lmio 2091319361@qq.com
Date: 2023-07-29 17:06:15
LastEditors: lmio 2091319361@qq.com
Description: 1161. 最大层内元素和
'''
from collections import deque
from typing import Optional

from utils.node import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        curr = 1
        res = 1
        maxSum = float('-inf')
        while q:
            sum = 0
            tmp = deque()
            while q:
                node = q.popleft()
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
                sum += node.val
            q = tmp
            if sum > maxSum:
                res = curr
                maxSum = sum
            curr += 1
        return res