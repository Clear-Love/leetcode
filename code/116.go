/*
 * @Author: lmio
 * @Date: 2023-02-08 00:30:36
 * @LastEditTime: 2023-03-21 20:22:21
 * @FilePath: /leetcode/code/116.go
 * @Description:116.填充每个节点的下一个右侧节点指针
 */
package code

import ."leetcode/code_struct"

func Connect(root *Node) *Node{
	node := root
	for node != nil {
		if node.Left == nil {
            return root
        }
		head := node
		for head != nil {
            
			head.Left.Next = head.Right
			if head.Next != nil {
				head.Right.Next = head.Next.Left
			}
			head = head.Next
		}
		node = node.Left
	}
	return root
}