/*
 * @Author: lmio
 * @Date: 2023-03-23 17:08:18
 * @LastEditTime: 2023-03-23 19:44:48
 * @FilePath: /leetcode/offer/06.go
 * @Description:剑指 Offer 06. 从尾到头打印链表
 */
package offer

import ."leetcode/code_struct"

func ReversePrint(head *ListNode) []int {
	res := []int{}
	var reserve func(node *ListNode)
	reserve = func(node *ListNode) {
		if node == nil {
			return
		}
		reserve(node.Next)
		res = append(res, node.Val)
	}
	reserve(head)
	return res
}