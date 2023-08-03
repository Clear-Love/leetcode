'''
Author: lmio 2091319361@qq.com
Date: 2023-08-03 19:46:06
LastEditors: lmio 2091319361@qq.com
Description: 面试题 02.05. 链表求和
'''

from utils.node import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        node = head
        carry = 0
        while l1 or l2:
            num1, num2 = 0, 0
            if l1:
                num1 = l1.val
                l1 = l1.next
            if l2:
                num2 = l2.val
                l2 = l2.next
            carry, num = divmod(num1 + num2 + carry, 10)
            node.next = ListNode(num)
            node = node.next
        if carry:
            node.next = ListNode(carry)
        return head.next