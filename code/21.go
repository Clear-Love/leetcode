/*
 * @Author: lmio
 * @Date: 2023-02-10 16:45:35
 * @LastEditTime: 2023-03-21 20:21:51
 * @FilePath: /leetcode/code/21.go
 * @Description:21.合并两个有序链表
 */
package code

import ."leetcode/code_struct"

func MergeTowList(list1 *ListNode, list2 *ListNode) *ListNode {
	head := &ListNode{}
	node := head
	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			node.Next = list1
			list1 = list1.Next
		}else {
			node.Next = list2
			list2 = list2.Next
		}
		node = node.Next
	}
	if list1 == nil {
		node.Next = list2
	}else {
		node.Next = list1
	}
	return head.Next
}