/*
 * @Author: lmio
 * @Date: 2023-04-06 09:35:31
 * @LastEditTime: 2023-08-21 21:42:19
 * @FilePath: /leetcode/code/300.go
 * @Description:300. 最长递增子序列
 */
package code

import "sort"

func LengthOfLIS(nums []int) int {
	stack := []int{nums[0]}
	for _, num := range nums[1:] {
		if num > stack[len(stack)-1] {
			stack = append(stack, num)
		} else {
			idx := sort.SearchInts(stack, num)
			stack[idx] = num
		}
	}
	return len(stack)
}