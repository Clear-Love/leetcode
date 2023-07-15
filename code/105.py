'''
Author: lmio 2091319361@qq.com
Date: 2023-07-08 18:11:45
LastEditors: lmio 2091319361@qq.com
Description: 105. 从前序与中序遍历序列构造二叉树
'''

from typing import List, Optional

from utils.node import TreeNode

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    def build(pre: List[int], ind: List[int]):
        if not pre:
            return None
        val = pre[0]
        i = ind.index(val)
        left = build(pre[1:i+1], ind[:i])
        right = build(pre[i+1:], ind[i+1:])
        return TreeNode(val, left, right)
    return build(preorder, inorder)