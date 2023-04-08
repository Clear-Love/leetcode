/*
 * @Author: lmio
 * @Date: 2023-04-08 10:38:44
 * @LastEditTime: 2023-04-08 10:45:50
 * @FilePath: /leetcode/offer/55-I.go
 * @Description:剑指 Offer 55 - I. 二叉树的深度
 */
package offer

import (
	. "leetcode/code_struct"
	"leetcode/utils"
)

func MaxDepth(root *TreeNode) int {
	var dfs func(node *TreeNode, depth int) int
	dfs = func(node *TreeNode, depth int) int {
		if node == nil {
			return depth-1
		}
		return utils.Max(dfs(node.Left, depth+1),dfs(node.Right, depth+1))
	}
	return dfs(root, 1)
}