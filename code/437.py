'''
Author: lmio 2091319361@qq.com
Date: 2023-07-29 15:41:40
LastEditors: lmio 2091319361@qq.com
Description: 437. 路径总和 III
'''

from collections import defaultdict
from typing import Optional
from utils.node import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 需要查找的前缀和
        preSum = defaultdict(int)
        preSum[targetSum] = 1
        sum = 0
        res = 0
        def dfs(node: TreeNode):
            nonlocal sum, res
            if not node:
                return
            sum += node.val
            res += preSum[sum]
            preSum[sum + targetSum]  += 1
            tmp = sum
            dfs(node.left)
            sum = tmp
            dfs(node.right)
            preSum[tmp + targetSum] -= 1
        dfs(root)
        return res