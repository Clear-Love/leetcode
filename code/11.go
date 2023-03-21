/*
 * @Author: lmio
 * @Date: 2023-02-21 22:22:06
 * @LastEditTime: 2023-02-21 22:30:36
 * @FilePath: /leetcode/code/11.go
 * @Description:11.盛最多的水
 */
package code

import (
	"leetcode/template"
)

func MaxArea(height []int) int {
	left, right := 0, len(height)-1
	maxarea := 0
	for left < right {
		if height[left] < height[right] {
			maxarea = template.Max(maxarea, height[left] * (right - left))
			left++
		}else {
			maxarea = template.Max(maxarea, height[right] * (right - left))
			right--
		}
	}
	return maxarea
}