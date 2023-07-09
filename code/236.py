'''
Author: lmio 2091319361@qq.com
Date: 2023-07-09 21:20:58
LastEditors: lmio 2091319361@qq.com
Description: 236. 二叉树的最近公共祖先
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def ancestor(node: TreeNode) -> TreeNode:
        if not node:
            return None
        if node == p or node == q:
            return node
        left = ancestor(node.left)
        right = ancestor(node.right)
        if left and right:
            return node
        elif left:
            return left
        elif right:
            return right
        return None
    return ancestor(root)