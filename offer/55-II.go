/*
 * @Author: lmio
 * @Date: 2023-04-08 10:47:10
 * @LastEditTime: 2023-04-08 11:15:57
 * @FilePath: /leetcode/offer/55-II.go
 * @Description:剑指 Offer 55 - II. 平衡二叉树
 */
package offer

import (
	. "leetcode/code_struct"
	"leetcode/utils"
)

func IsBalanced(root *TreeNode) bool {
	var dfs func(node *TreeNode, depth int) (int, bool)
	dfs = func(node *TreeNode, depth int) (int, bool) {
		if node == nil {
			return depth-1, true
		}
		kl, bl := dfs(node.Left, depth+1)
		kr, br := dfs(node.Right, depth+1)
		return utils.Max(kl, kr), utils.Abs(kl - kr) <= 1 && bl && br
	}
	_, res := dfs(root, 1)
	return res
}