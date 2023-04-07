/*
 * @Author: lmio
 * @Date: 2023-04-03 10:50:49
 * @LastEditTime: 2023-04-07 14:36:10
 * @FilePath: /leetcode/code/45.go
 * @Description:45.跳跃游戏II
 */
package code

import (
	"leetcode/utils"
	"math"
)

func Jump(nums []int) int {
	dp := make([]int, len(nums))
	for i := range dp {
		dp[i] = math.MaxInt
	}
	dp[0] = 0
	for i := 0; i < len(nums)-1; i++ {
		for j := i+1; j < len(nums) && j <= i+nums[i]; j++ {
			dp[j] = utils.Min(dp[j], dp[i] + 1)	
		}
	}
	return dp[len(nums)-1]
}