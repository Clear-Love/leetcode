/*
 * @Author: lmio
 * @Date: 2023-03-26 22:35:04
 * @LastEditTime: 2023-04-07 14:32:37
 * @FilePath: /leetcode/offer/53-I.go
 * @Description:剑指 Offer 53 - I. 在排序数组中查找数字 I
 */
package offer

import "leetcode/utils"

func Search(nums []int, target int) int {
	res := 0
	index := utils.Search_left(nums, target)
	for i := index; i < len(nums); i++ {
		if nums[i] != target {
			return res
		}
		res++
	}
	return res
}