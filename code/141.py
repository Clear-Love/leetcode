'''
Author: lmio 2091319361@qq.com
Date: 2023-07-07 17:57:35
LastEditors: lmio 2091319361@qq.com
Description: 141. 环形链表
'''

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False
    slow, fast = head, head.next
    while slow and fast:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next
    return False