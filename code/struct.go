/*
 * @Author: lmio
 * @Date: 2023-02-19 23:23:52
 * @LastEditTime: 2023-02-19 23:36:52
 * @FilePath: /leetcode/code/struct.go
 * @Description:leetcode数据结构
 */
package code

type ListNode struct {
    Val int
    Next *ListNode
}

type Node struct {
    Val int
    Left *Node
    Right *Node
    Next *Node
}