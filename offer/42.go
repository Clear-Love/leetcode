/*
 * @Author: lmio
 * @Date: 2023-03-30 08:06:22
 * @LastEditTime: 2023-04-07 14:30:59
 * @FilePath: /leetcode/offer/42.go
 * @Description:剑指 Offer 42. 连续子数组的最大和
 */
package offer

import "leetcode/utils"

func MaxSubArray(nums []int) int {
	n := len(nums)
	dp := make([]int, n)
	dp[0] = nums[0]
	res := dp[0]
	for i := 1; i < n; i++ {
		dp[i] = utils.Max(dp[i-1] + nums[i], nums[i])
		res = utils.Max(res, dp[i])
	}
	return res
}