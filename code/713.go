/*
 * @Author: lmio
 * @Date: 2023-02-22 18:15:00
 * @LastEditTime: 2023-04-07 14:36:57
 * @FilePath: /leetcode/code/713.go
 * @Description:713.乘积小于k的子数组
 */
package code

import "leetcode/utils"

func NumSubarrayProductLessThank(nums []int, k int) int {
	left, right := 0, 0
	sum := 1
	res := 0
	for left = range nums {
		right = utils.Max(left, right)
		for right < len(nums) {
			if sum * nums[right] >= k {
				break
			}
			sum *= nums[right]
			right++
		}
		res += right - left
		sum /= nums[left]
		if sum == 0 {
			sum = 1
		}
	}
	return res
}