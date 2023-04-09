/*
 * @Author: lmio
 * @Date: 2023-04-09 19:31:55
 * @LastEditTime: 2023-04-09 19:36:44
 * @FilePath: /leetcode/code/104.go
 * @Description:104. 二叉树的最大深度
 */
package code

import (
	. "leetcode/code_struct"
	"leetcode/utils"
)

func MaxDepth(root *TreeNode) int {
	var dfs func(*TreeNode, int) int
	dfs = func(node *TreeNode, depth int) int {
		if node == nil {
			return depth-1
		}
		return utils.Max(dfs(node.Left, depth+1), dfs(node.Right, depth+1))
	}
	return dfs(root, 1)
}