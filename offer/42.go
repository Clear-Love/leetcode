/*
 * @Author: lmio
 * @Date: 2023-03-30 08:06:22
 * @LastEditTime: 2023-03-30 08:26:19
 * @FilePath: /leetcode/offer/42.go
 * @Description:剑指 Offer 42. 连续子数组的最大和
 */
package offer

import "leetcode/template"

func MaxSubArray(nums []int) int {
	n := len(nums)
	dp := make([]int, n)
	dp[0] = nums[0]
	res := dp[0]
	for i := 1; i < n; i++ {
		dp[i] = template.Max(dp[i-1] + nums[i], nums[i])
		res = template.Max(res, dp[i])
	}
	return res
}