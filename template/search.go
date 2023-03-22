/*
 * @Author: lmio
 * @Date: 2023-02-03 05:29:24
 * @LastEditTime: 2023-03-22 14:34:14
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
