/*
 * @Author: lmio
 * @Date: 2023-02-05 21:33:59
 * @LastEditTime: 2023-02-19 23:36:11
 * @FilePath: /leetcode/code/876.go
 * @Description:876.链表的中间结点
 */
package code

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