/*
 * @Author: lmio
 * @Date: 2023-03-27 20:25:00
 * @LastEditTime: 2023-03-27 20:53:45
 * @FilePath: /leetcode/offer/32-III.go
 * @Description:剑指 Offer 32 - III. 从上到下打印二叉树 III
 */
package offer

import ."leetcode/code_struct"

func LevelOrderIII(root *TreeNode) [][]int {
	res := [][]int{}
	nodes := []*TreeNode{root}
	l2r := true
	var tempRes []int
	var tempNodes []*TreeNode
	var r2lPrint func()
	// 利用递归的特性从右往左
	r2lPrint = func() {
		if len(nodes) == 0 {
			return
		}
		node := nodes[len(nodes)-1]
		nodes = nodes[:len(nodes)-1]
		if node == nil {
			r2lPrint()
			return
		}
		tempRes = append(tempRes, node.Val)
		r2lPrint()
		tempNodes = append(tempNodes, node.Left, node.Right)
	}
	
	for len(nodes) != 0 {
		tempRes = make([]int, 0, len(nodes))
		tempNodes = make([]*TreeNode, 0, len(nodes)*2)
		if l2r {
			for len(nodes) != 0 {
				node := nodes[0]
				nodes = nodes[1:]
				
				if node == nil {
					continue
				}
				tempRes = append(tempRes, node.Val)
				tempNodes = append(tempNodes, node.Left, node.Right)
			}
		}else {
			r2lPrint()
		}
		l2r = !l2r
		res = append(res, tempRes)
		nodes = tempNodes
	}
	return res[0:len(res)-1]
}