/*
 * @Author: lmio
 * @Date: 2023-04-09 18:09:44
 * @LastEditTime: 2023-04-09 18:23:13
 * @FilePath: /leetcode/code/83.go
 * @Description:83. 删除排序链表中的重复元素
 */
package code

import ."leetcode/code_struct"

func DeleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
        return nil
    }
	pre := head
	cur := head.Next
	for cur != nil {
		if cur.Val == pre.Val {
			pre.Next = cur.Next
			cur = cur.Next
		}else {
			pre = pre.Next
			cur = cur.Next
		}
	}
    return head
}