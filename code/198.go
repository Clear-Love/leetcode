/*
 * @Author: lmio
 * @Date: 2023-02-11 21:09:24
 * @LastEditTime: 2023-04-02 15:46:24
 * @FilePath: /leetcode/code/198.go
 * @Description:198.打家劫舍
 */
package code

import "leetcode/template"

func RobI(nums []int) int {
	length := len(nums)
	if length == 1 {
		return nums[0]
	}else if length == 2 {
		return template.Max(nums[0], nums[1])
	}
	dp := []int{}
	dp = append(dp, nums[0], template.Max(nums[0], nums[1]))
	
	for i := 2; i < length; i++ {
		dp = append(dp, template.Max(dp[i-1], dp[i-2] + nums[i]))  
	}
	return dp[length-1]
}