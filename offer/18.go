/*
 * @Author: lmio
 * @Date: 2023-04-01 14:49:38
 * @LastEditTime: 2023-04-01 15:00:43
 * @FilePath: /leetcode/offer/18.go
 * @Description:剑指 Offer 18. 删除链表的节点
 */
package offer

import ."leetcode/code_struct"

func Delete(head *ListNode, val int) *ListNode {
	dummy := &ListNode{Next: head}
	pre := dummy
	node := head
	for node != nil {
		if node.Val == val {
			pre.Next = node.Next
		}
		pre = node
		node = node.Next
	}
	return dummy.Next
}