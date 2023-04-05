/*
 * @Author: lmio
 * @Date: 2023-04-05 17:38:02
 * @LastEditTime: 2023-04-05 18:01:37
 * @FilePath: /leetcode/offer/54.go
 * @Description:剑指 Offer 54. 二叉搜索树的第k大节点
 */
package offer

import ."leetcode/code_struct"

func KthLargest(root *TreeNode, k int) (res int) {
	n := 0
	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		dfs(node.Right)
		n++
		if n == k {
			res = node.Val
			return
		}
		dfs(node.Left)
	}
	return
}