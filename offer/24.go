/*
 * @Author: lmio
 * @Date: 2023-03-23 19:52:22
 * @LastEditTime: 2023-03-23 20:30:10
 * @FilePath: /leetcode/offer/24.go
 * @Description:剑指 Offer 24. 反转链表
 */
package offer

import (
	. "leetcode/code_struct"
)

func ReverseList(head *ListNode) *ListNode {
	var prev *ListNode
	node := head
	for node != nil {
		temp := node.Next
		node.Next = prev
		prev = node
		node = temp
	}
	return prev
}