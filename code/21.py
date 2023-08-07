'''
Author: lmio 2091319361@qq.com
Date: 2023-08-05 12:25:44
LastEditors: lmio 2091319361@qq.com
Description:21. 合并两个有序链表 
'''

from typing import Optional

from utils.node import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        return dummy.next