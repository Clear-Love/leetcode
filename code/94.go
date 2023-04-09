/*
 * @Author: lmio
 * @Date: 2023-04-09 18:56:28
 * @LastEditTime: 2023-04-09 18:59:54
 * @FilePath: /leetcode/code/94.go
 * @Description:94. 二叉树的中序遍历
 */
package code

import ."leetcode/code_struct"

func InorderTraversal(root *TreeNode) []int {
	res := []int{}
	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		dfs(node.Left)
		res = append(res, node.Val)
		dfs(node.Right)
	}
	dfs(root)
	return res
}