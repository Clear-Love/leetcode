/*
 * @Author: lmio
 * @Date: 2023-04-07 14:38:06
 * @LastEditTime: 2023-04-07 15:32:15
 * @FilePath: /leetcode/code/1143.go
 * @Description:1143. 最长公共子序列
 */
package code

import "leetcode/utils"

func LongestCommonSubsequence(text1 string, text2 string) int {
	n, m := len(text1)+1, len(text2)+1
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, m)
	}
	for i := 1; i < n; i++ {
		for j := 1; j < m; j++ {
			if text1[i-1] == text2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			}else {
				dp[i][j] = utils.Max(dp[i][j-1], dp[i-1][j]) 
			}
		}
	}
	return dp[n-1][m-1]
}