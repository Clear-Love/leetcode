'''
Author: lmio
Date: 2023-04-18 10:25:31
LastEditTime: 2023-07-14 20:12:36
FilePath: /leetcode/offer/37.py
Description: 剑指 Offer 37. 序列化二叉树
'''
import collections

from utils.node import TreeNode

class Codec:

    def serialize(self, root: TreeNode):
        nodes = collections.deque()
        nodes.append(root)
        res = []
        while nodes:
            node = nodes.popleft()
            if node:
                res.append(str(node.val))
                nodes.append(node.left)
                nodes.append(node.right)
            else:
                res.append("null")
        return ",".join(res)
        

    def deserialize(self, data: str):
        s = data.split(",")
        if s[0] == "null":
            return None
        root = TreeNode(s[0])
        nodes = collections.deque()
        nodes.append(root)
        i = 1
        while nodes:
            node = nodes.popleft()
            l, r = s[i], s[i+1]
            i += 2
            if l != "null":
                left = TreeNode(l)
                node.left = left
                nodes.append(left)
            if r != "null":
                right = TreeNode(r)
                node.right = right
                nodes.append(right)
        return root