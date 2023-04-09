/*
 * @Author: lmio
 * @Date: 2023-04-09 19:00:29
 * @LastEditTime: 2023-04-09 19:09:52
 * @FilePath: /leetcode/code/100.go
 * @Description:100. 相同的树
 */
package code

import ."leetcode/code_struct"

func IsSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	if p == nil || q == nil {
		return false
	}
	return p.Val == q.Val &&
		IsSameTree(p.Left, q.Left) &&
		IsSameTree(p.Right, q.Right)
}
