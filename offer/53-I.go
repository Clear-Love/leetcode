/*
 * @Author: lmio
 * @Date: 2023-03-26 22:35:04
 * @LastEditTime: 2023-03-26 23:42:31
 * @FilePath: /leetcode/offer/53.go
 * @Description:剑指 Offer 53 - I. 在排序数组中查找数字 I
 */
package offer

import "leetcode/template"

func Search(nums []int, target int) int {
	res := 0
	index := template.Search_left(nums, target)
	for i := index; i < len(nums); i++ {
		if nums[i] != target {
			return res
		}
		res++
	}
	return res
}