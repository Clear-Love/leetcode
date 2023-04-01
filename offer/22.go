/*
 * @Author: lmio
 * @Date: 2023-04-01 15:01:29
 * @LastEditTime: 2023-04-01 15:07:05
 * @FilePath: /leetcode/offer/22.go
 * @Description:剑指 Offer 22. 链表中倒数第k个节点
 */
package offer

import ."leetcode/code_struct"

func GetKthFromEnd(head *ListNode, k int) *ListNode {
	left, right := head, head
	for i := 0; i < k; i++ {
		if right == nil {
			return nil
		}
		right = right.Next
	}
	for right != nil {
		right = right.Next
		left = left.Next
	}
	return left
}