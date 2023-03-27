/*
 * @Author: lmio
 * @Date: 2023-03-27 18:12:25
 * @LastEditTime: 2023-03-27 20:11:20
 * @FilePath: /leetcode/offer/32-II.go
 * @Description:剑指 Offer 32 - II. 从上到下打印二叉树 II
 */
package offer

import ."leetcode/code_struct"

func LevelOrderII(root *TreeNode) [][]int {
	res := [][]int{}
	nodes := []*TreeNode{root}
	for len(nodes) != 0 {
		tempRes := make([]int, 0, len(nodes))
		tempNodes := make([]*TreeNode, 0, len(nodes)*2)
		for len(nodes) != 0 {
			node := nodes[0]
			nodes = nodes[1:]
			if node == nil {
				continue
			}
			tempRes = append(tempRes, node.Val)
			tempNodes = append(tempNodes, node.Left, node.Right)
		}
		res = append(res, tempRes)
		nodes = tempNodes
	}
	return res[0:len(res)-1]
}  