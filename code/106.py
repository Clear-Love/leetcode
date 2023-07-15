'''
Author: lmio 2091319361@qq.com
Date: 2023-07-08 21:14:13
LastEditors: lmio 2091319361@qq.com
Description: 106. 从中序与后序遍历序列构造二叉树
'''

from typing import List, Optional

from utils.node import TreeNode

def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def build(ind: List[int], post: List[int]):
        if not ind:
            return None
        i = ind.index(post[-1])
        val = ind[i]
        left = build(ind[:i], post[:i])
        right = build(ind[i+1:], post[i:-1])
        return TreeNode(val, left, right)
    return build(inorder, postorder)