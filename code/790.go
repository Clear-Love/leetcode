/*
 * @Author: lmio
 * @Date: 2023-03-09 22:50:38
 * @LastEditTime: 2023-03-21 23:09:13
 * @FilePath: /leetcode/code/790.go
 * @Description:790.多米诺和托米诺平铺
 */
package code


/**
 * @description: 简单状态机，每一列定义四个状态
 * @param {int} n
 * @return {*}
 */
func NumTilings(n int) int {
	var mod int = 1e9 + 7
	dp := make([][4]int, n+1)
	dp[0][3] = 1
	for i := 1; i <= n; i++ {
		dp[i][0] = dp[i-1][3] % mod
		dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod
		dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % mod
		dp[i][3] = (dp[i][2] + dp[i-1][2] + dp[i-1][3]) % mod
	}
	return dp[n][3]
}