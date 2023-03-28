/*
 * @Author: lmio
 * @Date: 2023-03-28 14:27:12
 * @LastEditTime: 2023-03-28 14:49:46
 * @FilePath: /leetcode/offer/28.go
 * @Description:剑指 Offer 28. 对称的二叉树
 */
package offer

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
	return l.Val == r.Val && check(l.Left, r.Right) &&check(l.Right, r.Left)
}