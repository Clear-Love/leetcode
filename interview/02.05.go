/*
 * @Author: lmio
 * @Date: 2023-03-28 23:32:28
 * @LastEditTime: 2023-08-03 20:50:15
 * @FilePath: /leetcode/interview/02.05.go
 * @Description:面试题 02.05. 链表求和
 */
package interview

import . "leetcode/code_struct"

func AddTwoNumbers(l1, l2 *ListNode) *ListNode {
	carry := 0
	head := &ListNode{}
	node := head
	for l1 != nil || l2 != nil {
		num1, num2 := 0, 0
		if l1 != nil {
			num1 = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			num2 = l2.Val
			l2 = l2.Next
		}
		sum := num1 + num2 + carry
		node.Next = &ListNode{Val: sum % 10}
		carry = sum / 10
		node = node.Next
	}

	if carry != 0 {
		node.Next = &ListNode{Val: carry}
	}
	return head.Next
}
