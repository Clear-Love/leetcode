'''
Author: lmio
Date: 2023-04-09 12:56:08
LastEditTime: 2023-04-09 13:16:29
FilePath: /leetcode/offer/68-I.py
Description: 剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
    