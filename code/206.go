/*
 * @Author: lmio
 * @Date: 2023-02-10 17:06:37
 * @LastEditTime: 2023-02-19 23:41:07
 * @FilePath: /leetcode/code/206.go
 * @Description:206.反转链表
 */
package code

func ReverseList(head *ListNode) *ListNode {
	node := head
	var prev *ListNode
	for node != nil {
		temp := node.Next
		node.Next = prev
		prev = node
		node = temp
	}
	return prev
}
