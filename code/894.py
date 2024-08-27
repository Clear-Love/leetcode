'''
Author: lmio 2091319361@qq.com
Date: 2024-04-02 18:47:35
LastEditors: lmio 2091319361@qq.com
Description: 894. 所有可能的真二叉树
'''


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

MX = 11
dp = [[] for _ in range(MX)]
dp[1] = [TreeNode()]
for i in range(2, MX):  # 计算 dp[i]
    dp[i] = [TreeNode(0, left, right)
            for j in range(1, i)  # 枚举左子树叶子数
            for left in dp[j]  #  枚举左子树
            for right in dp[i - j]]  # 枚举右子树


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return dp[n//2+1] if n&1 else []