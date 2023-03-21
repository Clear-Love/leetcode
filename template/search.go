/*
 * @Author: lmio
 * @Date: 2023-02-03 05:29:24
 * @LastEditTime: 2023-02-19 23:21:48
 * @FilePath: /leetcode/template/search.go
 * @Description:二分搜索及其变种
 */
package template

func Search_left(nums []int, target int) int {
	left, right:= 0, len(nums)-1
	for left < right {
		mid := (left + right + 1) >> 1
		if nums[mid] > target {
			right = mid - 1
		}else {
			left = mid
		}
	}
	return left
}

func Search_right(nums []int, target int) int {
	left, right:= 0, len(nums)-1
	for left < right {
		mid := (left + right) >> 1
		if nums[mid] < target {
			left = mid + 1
		}else {
			right = mid
		}
	}
	return left
}

func Search_right_(nums []int, target int) int {
	left, right:= 0, len(nums)-1
	for left < right {
		mid := (left + right) >> 1
		if nums[mid] <= target {
			left = mid + 1
		}else {
			right = mid
		}
	}
	return left
}