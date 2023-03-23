/*
 * @Author: lmio
 * @Date: 2023-03-23 20:43:38
 * @LastEditTime: 2023-03-23 21:22:48
 * @FilePath: /leetcode/offer/35.go
 * @Description:剑指 Offer 35. 复杂链表的复制
 */
package offer

type Node struct {
    Val int
    Next *Node
    Random *Node
}

func CopyRandomList(head *Node) *Node {
	var copy func(node *Node) *Node
	nodes := map[*Node]*Node{}
	copy = func(node *Node) *Node {
		if node == nil {
			return nil
		}
		val, ok := nodes[node]
		if ok {
			return val
		}
		curr := &Node{}
		nodes[node] = curr
		curr.Val = node.Val
		curr.Next = copy(node.Next)
		curr.Random = copy(node.Random)
		return curr
	}
	return copy(head)
}