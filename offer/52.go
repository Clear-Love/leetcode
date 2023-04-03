/*
 * @Author: lmio
 * @Date: 2023-04-02 14:44:39
 * @LastEditTime: 2023-04-02 15:24:49
 * @FilePath: /leetcode/offer/52.go
 * @Description:剑指 Offer 52. 两个链表的第一个公共节点
 */
package offer

import ."leetcode/code_struct"

func GetIntersectionNode(headA, headB *ListNode) *ListNode {
	listMap := map[*ListNode]bool{}
	iscontain := func(node *ListNode) bool {
		_, ok := listMap[node]
		if ok {
			return true
		}
		listMap[node] = true
		return false
	}
	for headA != nil || headB != nil {
		if headA != nil {
			if iscontain(headA) {
				return headA
			}
			headA = headA.Next
		}
		if headB != nil {
			if iscontain(headB) {
				return headB
			}
			headB = headB.Next
		}
	}
	return nil
}