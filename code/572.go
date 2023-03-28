/*
 * @Author: lmio
 * @Date: 2023-03-28 15:55:30
 * @LastEditTime: 2023-03-28 16:04:13
 * @FilePath: /leetcode/code/572.go
 * @Description:572. 另一棵树的子树
 */
package code

import ."leetcode/code_struct"

func IsSubtree(root *TreeNode, subRoot *TreeNode) bool {
	if root == nil || subRoot== nil {
			return false
		}
	return  containNode(root, subRoot) ||
			IsSubtree(root.Left, subRoot) ||
			IsSubtree(root.Right, subRoot)
}

func containNode(A *TreeNode, B *TreeNode) bool {
	if A == nil && B == nil {
		return true
	}
	if A == nil || B == nil {
		return false
	}
	return A.Val == B.Val && containNode(A.Left, B.Left) && containNode(A.Right, B.Right)
}