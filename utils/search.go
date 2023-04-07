/*
 * @Author: lmio
 * @Date: 2023-02-03 05:29:24
 * @LastEditTime: 2023-04-07 14:30:01
 * @FilePath: /leetcode/utils/search.go
 * @Description:二分搜索及其变种
 */
package utils

/**
 * @description: 返回等于目标值下标(若有多个，返回最左边的)
 * @param {[]int} nums
 * @param {int} target
 * @return {*}
 */
func Search_left(nums []int, target int) int {
	if len(nums) == 0 {
		return -1
	}
	left, right:= 0, len(nums)-1
	for left < right {
		mid := (left + right) >> 1
		if nums[mid] < target {
			left = mid + 1
		}else {
			right = mid
		}
	}
	if nums[left] != target {
		return -1
	}
	return left
}

/**
 * @description: 返回等于目标值的下标(若有多个返回最右边的)
 * @param {[]int} nums
 * @param {int} target
 * @return {*}
 */
func Search_right(nums []int, target int) int {
	if len(nums) == 0 {
		return -1
	}
	left, right:= 0, len(nums)-1
	for left < right {
		mid := (left + right + 1) >> 1
		if nums[mid] > target {
			right = mid - 1
		}else {
			left = mid
		}
	}
	if nums[left] != target {
		return -1
	}
	return left
}

/**
 * @description: 找到数组中出现频率最高的数
 * @param {[]int} m
 * @return {*}
 */
func MostFrequentValue(m []int) int {
    // 创建一个字典，用于跟踪每个值的出现次数
    counts := make(map[int]int)

	maxCount := 0
    mostFrequentValue := 0
    // 遍历映射并递增每个值的计数器
    for _, v := range m {
        counts[v]++
		if counts[v] > maxCount {
            maxCount = counts[v]
            mostFrequentValue = v
        }
    }

    // 返回计数器最高的值
    return mostFrequentValue
}
