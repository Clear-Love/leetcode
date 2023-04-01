/*
 * @Author: lmio
 * @Date: 2023-03-30 08:27:42
 * @LastEditTime: 2023-03-30 08:39:59
 * @FilePath: /leetcode/offer/47.go
 * @Description:剑指 Offer 47. 礼物的最大价值
 */
package offer

import "leetcode/template"

func MaxValue(grid [][]int) int {
	n, m := len(grid), len(grid[0])
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, m)
	}
	dp[0][0] = grid[0][0]
	for i := 1; i < n; i++ {
		dp[i][0] = dp[i-1][0] + grid[i][0]
	}
	for j := 1; j < m; j++ {
		dp[0][j] = dp[0][j-1] + grid[0][j]
	}
	for i := 1; i < n; i++ {
		for j := 1; j < m; j++ {
			dp[i][j] = template.Max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
		}
	}
	return dp[n-1][m-1]
}