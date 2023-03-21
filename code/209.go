/*
 * @Author: lmio
 * @Date: 2023-02-22 20:14:19
 * @LastEditTime: 2023-02-22 20:38:14
 * @FilePath: /leetcode/code/209.go
 * @Description:209.长度最小的子数组
 */
package code

import (
	"leetcode/template"
	"math"
)

func MinSubArrayLen(target int, nums []int) int {
	left, right := 0, 0
	sum := 0
	res := math.MaxInt
	for left = range nums {
		right = template.Max(left, right)
		for right < len(nums) && sum < target {
			sum += nums[right]
			right++
		}
		if sum < target {
			if left == 0 {
				return 0
			}
			return res
		}
		length := right - left
		if length < res {
			res = length
		}
		sum -= nums[left]
	}
	return res
}