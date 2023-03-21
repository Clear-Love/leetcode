/*
 * @Author: lmio
 * @Date: 2023-02-07 23:52:37
 * @LastEditTime: 2023-02-19 23:29:16
 * @FilePath: /leetcode/code/617.go
 * @Description:617.合并二叉树
 */
package code

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}
 

func MergeTrees(root1 *TreeNode, root2 *TreeNode) *TreeNode {
	if root1 == nil && root2 == nil {
		return nil
	}
	if root1 == nil {
		return root2
	}
	if root2 == nil {
		return root1
	}
	var node TreeNode
	node.Val = root1.Val + root2.Val
	node.Left = MergeTrees(root1.Left, root2.Left)
	node.Right = MergeTrees(root1.Right, root2.Right)
	return &node
}