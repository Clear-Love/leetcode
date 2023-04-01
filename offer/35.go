/*
 * @Author: lmio
 * @Date: 2023-03-23 20:43:38
 * @LastEditTime: 2023-04-01 14:21:14
 * @FilePath: /leetcode/offer/35.go
 * @Description:剑指 Offer 35. 复杂链表的复制
 */
package offer

import ."leetcode/code_struct"

func CopyRandomList(head *Node_) *Node_ {
	var copy func(node *Node_) *Node_
	nodes := map[*Node_]*Node_{}
	copy = func(node *Node_) *Node_ {
		if node == nil {
			return nil
		}
		val, ok := nodes[node]
		if ok {
			return val
		}
		curr := &Node_{}
		nodes[node] = curr
		curr.Val = node.Val
		curr.Next = copy(node.Next)
		curr.Random = copy(node.Random)
		return curr
	}
	return copy(head)
}