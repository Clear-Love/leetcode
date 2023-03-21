/*
 * @Author: lmio
 * @Date: 2023-02-12 21:01:30
 * @LastEditTime: 2023-02-19 23:36:35
 * @FilePath: /leetcode/code/1480.go
 * @Description:1480.一维数组的动态和
 */
package code

func RunningSum(nums []int) []int {
	for i := 1; i < len(nums); i++ {
		nums[i] += nums[i-1]
	}
	return nums
}