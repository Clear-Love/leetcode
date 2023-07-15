'''
Author: lmio 2091319361@qq.com
Date: 2023-07-14 19:58:29
LastEditors: lmio 2091319361@qq.com
Description: 108. 将有序数组转换为二叉搜索树
'''
from typing import List, Optional

from utils.node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
