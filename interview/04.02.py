'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 13:01:00
LastEditors: lmio 2091319361@qq.com
Description: 面试题 04.02. 最小树
'''

from typing import List

from utils.node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        n = len(nums)
        mid = n >> 1
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root