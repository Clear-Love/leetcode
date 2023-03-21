/*
 * @Author: lmio
 * @Date: 2023-02-11 22:17:01
 * @LastEditTime: 2023-02-19 23:27:32
 * @FilePath: /leetcode/code/120.go
 * @Description:120.三角形最小路径和
 */
package code

func MinimumTotal(triangle [][]int) int {
	n := len(triangle)
	dp := make([]int, 0)
	Min := func(x, y int) int {
		if x < y {
			return x
		}
		return y
	}
	dp = append(dp, triangle[n-1]...)
	for i := n-2; i >= 0; i-- {
		for j := 0; j < len(triangle[i]); j++ {
			val := triangle[i][j]
			dp[j] = Min(dp[j]+val, dp[j+1]+val)
		}
	}
	return dp[0]
}