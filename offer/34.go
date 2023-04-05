/*
 * @Author: lmio
 * @Date: 2023-04-05 16:37:21
 * @LastEditTime: 2023-04-05 16:58:42
 * @FilePath: /leetcode/offer/34.go
 * @Description:剑指 Offer 34. 二叉树中和为某一值的路径
 */
package offer

import ."leetcode/code_struct"

func PathSum(root *TreeNode, target int) [][]int {
	res := [][]int{}
	ans := []int{}
	sum := 0
	var backtarck func(node *TreeNode)
	backtarck = func(node *TreeNode) {
		if node == nil {
			return
		}
		sum += node.Val
		ans = append(ans, node.Val)
		if sum == target && node.Left == nil && node.Right == nil {
			res = append(res, append([]int{}, ans...))
			sum -= node.Val
			ans = ans[:len(ans)-1]
			return
		}
		backtarck(node.Left)
		backtarck(node.Right)
		sum -= node.Val
		ans = ans[:len(ans)-1]
	}
	backtarck(root)
	return res
}