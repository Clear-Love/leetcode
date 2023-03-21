/*
 * @Author: lmio
 * @Date: 2023-02-19 23:23:52
 * @LastEditTime: 2023-03-21 20:19:07
 * @FilePath: /leetcode/code_struct/Node.go
 * @Description:leetcode数据结构
 */
package code_struct


/**
 * @description: 链表结点
 * @return {*}
 */
type ListNode struct {
    Val int
    Next *ListNode
}

/**
 * @description: 二叉树结点
 * @return {*}
 */
type Node struct {
    Val int
    Left *Node
    Right *Node
    Next *Node
}