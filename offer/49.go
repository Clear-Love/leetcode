/*
 * @Author: lmio
 * @Date: 2023-04-20 08:26:45
 * @LastEditTime: 2023-04-20 09:14:12
 * @FilePath: /leetcode/offer/49.go
 * @Description:剑指 Offer 49. 丑数
 */
package offer

import "leetcode/utils"

func NthUglyNumber(n int) int {
	p2, p3, p5 := 0, 0, 0
	dp := make([]int, n)
	dp[0] = 1
	for i := 1; i < n; i++ {
		dp[i] = utils.Min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
		for dp[i] == dp[p2]*2{
			p2++
		}
		for dp[i] == dp[p3]*3 {
			p3++
		}
		for dp[i] == dp[p5]*5 {
			p5++
		}
	}
	return dp[n-1]
}