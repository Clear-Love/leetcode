/*
 * @Author: lmio
 * @Date: 2023-02-13 21:55:46
 * @LastEditTime: 2023-02-19 23:26:37
 * @FilePath: /leetcode/code/34.go
 * @Description:34.在排序数组中查找元素的第一个和最后一个位置
 */
package code

import "sort"

func SearchRange(nums []int, target int) []int {
	left := sort.SearchInts(nums, target)
	//如果未找到目标值
	if left == len(nums) || nums[left] != target {
		return []int{-1, -1}
	}
	right := sort.SearchInts(nums, target + 1) - 1
	return []int{left, right}
}