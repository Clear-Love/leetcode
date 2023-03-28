/*
 * @Author: lmio
 * @Date: 2023-03-28 12:53:30
 * @LastEditTime: 2023-03-28 13:20:29
 * @FilePath: /leetcode/offer/26.go
 * @Description:剑指 Offer 26. 树的子结构
 */
package offer

import ."leetcode/code_struct"

func IsSubStructure(A *TreeNode, B *TreeNode) bool {
	if A == nil || B == nil {
		return false
	}
	return  containNode(A, B) ||
			IsSubStructure(A.Left, B) ||
			IsSubStructure(A.Right, B)
}

func containNode(A *TreeNode, B *TreeNode) bool {
	if B == nil {
		return true
	}
	if A == nil {
		return false
	}
	return A.Val == B.Val && containNode(A.Left, B.Left) && containNode(A.Right, B.Right)
}