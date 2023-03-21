/*
 * @Author: lmio
 * @Date: 2023-03-09 22:43:05
 * @LastEditTime: 2023-03-09 22:49:55
 * @FilePath: /leetcode/code/1920.go
 * @Description:1920.基于排列构建数组
 */
package code 

func BuildArray(nums []int) []int {
	ans := make([]int, len(nums))
	for i := range nums {
		ans[i] = nums[nums[i]]
	}
	return ans
}