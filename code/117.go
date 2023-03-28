/*
 * @Author: lmio
 * @Date: 2023-03-28 14:52:10
 * @LastEditTime: 2023-03-28 15:54:41
 * @FilePath: /leetcode/code/117.go
 * @Description:117. 填充每个节点的下一个右侧节点指针 II
 */
package code

import ."leetcode/code_struct"

func ConnectII(root *Node) *Node {
	if root == nil {
		return nil
	}
	nodes := []*Node{root}
	for len(nodes) != 0 {
		tempNodes := []*Node{}
		for len(nodes) != 0 {
			node := nodes[0]
			nodes = nodes[1:]
			if node.Left != nil {
				tempNodes = append(tempNodes, node.Left)
			}
			if node.Right != nil {
				tempNodes = append(tempNodes, node.Right)
			}
		}
		link(tempNodes)
		nodes = tempNodes
	}
	return root
}

func link(nodes []*Node) {
	if len(nodes) == 0 {
		return
	}
	node := nodes[0]
	nodes = nodes[1:]
	for len(nodes) != 0 {
		node.Next = nodes[0]
		node = nodes[0]
		nodes = nodes[1:]
	}
}