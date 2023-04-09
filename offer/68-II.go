/*
 * @Author: lmio
 * @Date: 2023-04-09 13:17:28
 * @LastEditTime: 2023-04-09 13:28:39
 * @FilePath: /leetcode/offer/68-II.go
 * @Description:剑指 Offer 68 - II. 二叉树的最近公共祖先
 */
package offer

import ."leetcode/code_struct"

func LowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil {
        return nil
    }
    if root.Val == p.Val || root.Val == q.Val {
        return root
    }
    left := LowestCommonAncestor(root.Left, p, q)
    right := LowestCommonAncestor(root.Right, p, q)
    if left != nil && right != nil {
        return root
    }
    if left == nil {
        return right
    }
    return left
}