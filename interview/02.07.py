'''
Author: lmio 2091319361@qq.com
Date: 2023-08-03 21:01:20
LastEditors: lmio 2091319361@qq.com
Description: 
'''
from utils.node import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        n, m = 0, 0
        curA, curB = headA, headB
        while curA:
            curA = curA.next
            n += 1
        while curB:
            curB = curB.next
            m += 1
        i, j = 0, 0
        if n > m:
            i = n-m
        else:
            j = m -n
        curA, curB = headA, headB
        for _ in range(i):
            curA = curA.next
        for _ in range(j):
            curB = curB.next
        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None