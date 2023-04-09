/*
 * @Author: lmio
 * @Date: 2023-04-09 19:11:03
 * @LastEditTime: 2023-04-09 19:31:22
 * @FilePath: /leetcode/code/101.go
 * @Description:101. 对称二叉树
 */
package code

import ."leetcode/code_struct"

func IsSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return check(root, root)
}

func check(l, r *TreeNode) bool {
	if l == nil && r == nil {
		return true
	}else if l == nil || r == nil {
		return false
	}
	return l.Val == r.Val && check(l.Left, r.Right) && check(l.Right, r.Left)
}