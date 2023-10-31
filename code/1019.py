'''
Author: lmio 2091319361@qq.com
Date: 2023-10-26 22:35:43
LastEditors: lmio 2091319361@qq.com
Description: 1019. 链表中的下一个更大节点
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

from utils.node import ListNode


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        stack = []
        node = head
        i = 0
        nums = []
        while node:
            v = node.val
            while stack and nums[stack[-1]] < v:
                res[stack.pop()] = v
            stack.append(i)
            res.append(0)
            nums.append(v)
            node = node.next
            i += 1
        return res