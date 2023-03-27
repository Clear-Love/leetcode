/*
 * @Author: lmio
 * @Date: 2023-03-27 18:02:01
 * @LastEditTime: 2023-03-27 18:12:15
 * @FilePath: /leetcode/offer/32-I.go
 * @Description:剑指 Offer 32 - I. 从上到下打印二叉树
 */
package offer

import ."leetcode/code_struct"

func LevelOrder(root *TreeNode) []int {
	res := []int{}
	nodes := []*TreeNode{root}
	for len(nodes) != 0 {
		node := nodes[0]
		nodes = nodes[1:]
		if node == nil {
			continue
		}
		res = append(res, node.Val)
		nodes = append(nodes, node.Left, node.Right)
	}
	return res
}