/*
 * @Author: lmio
 * @Date: 2023-02-05 21:33:59
 * @LastEditTime: 2023-03-21 20:23:14
 * @FilePath: /leetcode/code/876.go
 * @Description:876.链表的中间结点
 */
package code

import ."leetcode/code_struct"

func MiddleNode(head *ListNode) *ListNode {
	slow, fast := head, head.Next
	for fast != nil {
		slow = slow.Next
		fast = fast.Next
		if fast != nil {
			fast = fast.Next
		}
	}
	return slow
}