'''
Author: lmio 2091319361@qq.com
Date: 2023-07-08 16:05:14
LastEditors: lmio 2091319361@qq.com
Description: 86. 分隔链表
'''

from typing import Optional

from utils.node import ListNode

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    p=small=ListNode(0)
    q=large=ListNode(0)
    while head:
        if head.val<x:
            small.next=head
            small=small.next
        else:
            large.next=head
            large=large.next
        head=head.next
    large.next=None
    small.next=q.next
    return p.next