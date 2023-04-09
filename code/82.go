/*
 * @Author: lmio
 * @Date: 2023-02-20 21:47:12
 * @LastEditTime: 2023-04-09 18:11:18
 * @FilePath: /leetcode/code/82.go
 * @Description:82.删除有序链表中的重复元素II
 */
package code

import ."leetcode/code_struct"

func DeleteDuplicatesII(head *ListNode) *ListNode {
	if head == nil {
        return nil
    }

    dummy := &ListNode{Val: 0, Next: head}

    cur := dummy
    for cur.Next != nil && cur.Next.Next != nil {
        if cur.Next.Val == cur.Next.Next.Val {
            x := cur.Next.Val
            for cur.Next != nil && cur.Next.Val == x {
                cur.Next = cur.Next.Next
            }
        } else {
            cur = cur.Next
        }
    }

    return dummy.Next
}