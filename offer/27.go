/*
 * @Author: lmio
 * @Date: 2023-03-28 14:20:32
 * @LastEditTime: 2023-03-28 14:24:55
 * @FilePath: /leetcode/offer/27.go
 * @Description:剑指 Offer 27. 二叉树的镜像
 */
package offer

import ."leetcode/code_struct"

func MirrorTree(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	node := &TreeNode{Val: root.Val}
	node.Left, node.Right = MirrorTree(root.Right), MirrorTree(root.Left)
	return node
}