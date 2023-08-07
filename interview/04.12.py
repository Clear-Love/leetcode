'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 16:42:13
LastEditors: lmio 2091319361@qq.com
Description:面试题 04.12. 求和路径 
'''

from collections import defaultdict
from utils.node import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        nums = defaultdict(int)
        nums[sum] = 1
        res = 0
        s = 0
        def dfs(node: TreeNode):
            nonlocal res, s
            if not node:
                return
            s += node.val
            res += nums[s]
            nums[sum+s] += 1
            dfs(node.left)
            dfs(node.right)
            nums[sum+s] -= 1
            s -= node.val
        dfs(root)
        return res