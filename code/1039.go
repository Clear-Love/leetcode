/*
 * @Author: lmio
 * @Date: 2023-04-02 17:53:48
 * @LastEditTime: 2023-04-07 14:33:33
 * @FilePath: /leetcode/code/1039.go
 * @Description:1039. 多边形三角剖分的最低得分
 */
package code

import (
	."leetcode/utils"
	"math"
)

func MinScoreTriangulation(values []int) int {
	n := len(values)
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for i := n-3; i >= 0; i-- {
		for j := i+2; j < n; j++ {
			dp[i][j] = math.MaxInt
			for k := i+1; k < j; k++ {
				dp[i][j] = Min(dp[i][j], dp[i][k] + values[i]*values[j]*values[k] + dp[k][j])
			}
		}
	}
	return dp[0][n-1]
}