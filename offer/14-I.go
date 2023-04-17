/*
 * @Author: lmio
 * @Date: 2023-04-14 10:46:09
 * @LastEditTime: 2023-04-17 21:29:32
 * @FilePath: /leetcode/offer/14-I.go
 * @Description:剑指 Offer 14- I. 剪绳子
 */
package offer

import "leetcode/utils"

func CuttingRopeI(n int) int {
	dp := make([]int, n+1)
	dp[1] = 1
	for i := 2; i < len(dp); i++ {
		for j := 1; j < i; j++ {
			dp[i] = utils.Max(dp[i], j*(i-j), dp[j]*(i-j))
		}
	}
	return dp[n]
}