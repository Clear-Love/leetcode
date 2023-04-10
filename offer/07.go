/*
 * @Author: lmio
 * @Date: 2023-04-10 07:58:11
 * @LastEditTime: 2023-04-10 08:14:42
 * @FilePath: /leetcode/offer/07.go
 * @Description:剑指 Offer 07. 重建二叉树
 */
package offer

import ."leetcode/code_struct"

func BuildTree(preorder []int, inorder []int) *TreeNode {
	if len(preorder) == 0 {
        return nil
    }
    root := &TreeNode{Val: preorder[0], Left: nil, Right: nil}
    i := 0
	// 找到左右子树的分界点
    for ; i < len(inorder); i++ {
        if inorder[i] == preorder[0] {
            break
        }
    }
    root.Left = BuildTree(preorder[1:i+1], inorder[:i])
    root.Right = BuildTree(preorder[i+1:], inorder[i+1:])
    return root
}