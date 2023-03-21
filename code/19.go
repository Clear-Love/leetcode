/*
 * @Author: lmio
 * @Date: 2023-02-05 21:43:03
 * @LastEditTime: 2023-02-19 23:25:29
 * @FilePath: /leetcode/code/19.go
 * @Description:19.删除链表的倒数第N个结点
 */
package code

func RemoveNthFromEnd(head *ListNode, n int) *ListNode {
	right := head
	left := &ListNode{0, head}
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