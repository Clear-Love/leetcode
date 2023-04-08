/*
 * @Author: lmio
 * @Date: 2023-04-08 14:52:05
 * @LastEditTime: 2023-04-08 14:59:53
 * @FilePath: /leetcode/code/343.go
 * @Description:343. 整数拆分
 */
package code

import "leetcode/utils"

func IntegerBreak(n int) int {
	// 表示整数i拆分的最大乘积
	dp := make([]int, n+1)
	dp[1] = 1
	for i := 2; i < len(dp); i++ {
		for j := 1; j < i; j++ {
			dp[i] = utils.Max(dp[j]*(i-j), dp[i])
		}
	}
	return dp[n]
}