'''
Author: lmio
Date: 2023-04-09 12:56:08
LastEditTime: 2023-07-14 20:15:17
FilePath: /leetcode/offer/68-I.py
Description: 剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
'''

from utils.node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root
        while True:
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor
    