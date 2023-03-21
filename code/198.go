/*
 * @Author: lmio
 * @Date: 2023-02-11 21:09:24
 * @LastEditTime: 2023-02-19 23:28:16
 * @FilePath: /leetcode/code/198.go
 * @Description:198.打家劫舍
 */
package code

func Rob(nums []int) int {
	length := len(nums)
	Max := func (x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	if length == 1 {
		return nums[0]
	}else if length == 2 {
		return Max(nums[0], nums[1])
	}
	dp := []int{}
	dp = append(dp, nums[0], Max(nums[0], nums[1]))
	
	for i := 2; i < length; i++ {
		dp = append(dp, Max(dp[i-1], dp[i-2] + nums[i]))  
	}
	return dp[length-1]
}