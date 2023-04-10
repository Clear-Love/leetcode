/*
 * @Author: lmio
 * @Date: 2023-04-10 08:27:33
 * @LastEditTime: 2023-04-10 08:52:07
 * @FilePath: /leetcode/offer/33.go
 * @Description:剑指 Offer 33. 二叉搜索树的后序遍历序列
 */
package offer

func VerifyPostorder(postorder []int) bool {
	if len(postorder) == 0 {
		return true
	}
	root := postorder[len(postorder)-1]
	i := 0
	for i < len(postorder) && postorder[i] < root {
		i++
	}
	left := postorder[:i]
	right := postorder[i:len(postorder)-1]
	for i := 0; i < len(right); i++ {
		if	right[i] < root {
			return false
		}
	}
	return VerifyPostorder(left) && VerifyPostorder(right)
}