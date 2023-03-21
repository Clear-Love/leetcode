/*
 * @Author: lmio
 * @Date: 2023-02-13 22:29:16
 * @LastEditTime: 2023-02-19 23:26:30
 * @FilePath: /leetcode/code/33.go
 * @Description:33.搜索旋转升序数组
 */
package code

import "sort"

func Search_33(nums []int, target int) int {
	left  := 0
	right := len(nums)-1
	start := nums[0]
	for left < right {
		mid := (left+right+1) >> 1
		// 右侧有序
		if nums[mid] < start {
			right = mid - 1
		}else {
			left = mid
		}
	}
	res := left + 1
	if target < start {
		res += sort.SearchInts(nums[left+1:], target)
	}else {
		res = sort.SearchInts(nums[:left+1], target)
	}
	if res == len(nums) || nums[res] != target {
		return -1
	}
	return res
}