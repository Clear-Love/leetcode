/*
 * @Author: lmio
 * @Date: 2023-02-05 21:43:03
 * @LastEditTime: 2023-03-23 23:11:57
 * @FilePath: /leetcode/code/19.go
 * @Description:19.删除链表的倒数第N个结点
 */
package code

import . "leetcode/code_struct"

func RemoveNthFromEnd(head *ListNode, n int) *ListNode {
	right := head
	left := &ListNode{Val: 0, Next: head}
	for i := 0; i < n ; i++ {
			right = right.Next
	}
	
	for right != nil {
		right = right.Next
		left = left.Next
	}
	if left.Next == head {
		head = head.Next
	}else {
		left.Next = left.Next.Next
	}
	return head
}