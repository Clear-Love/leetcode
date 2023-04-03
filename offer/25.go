/*
 * @Author: lmio
 * @Date: 2023-04-02 14:37:16
 * @LastEditTime: 2023-04-02 14:42:54
 * @FilePath: /leetcode/offer/25.go
 * @Description:剑指 Offer 25. 合并两个排序的链表
 */
package offer

import ."leetcode/code_struct"

func MergeTwoLists(l1, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	node := dummy
	for l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
			node.Next = l1
			l1 = l1.Next
		}else {
			node.Next = l2
			l2 = l2.Next
		}
		node = node.Next
	}
	if l1 == nil {
		node.Next = l2
	}else {
		node.Next = l1
	}
	return dummy.Next
}