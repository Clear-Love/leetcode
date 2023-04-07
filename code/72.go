/*
 * @Author: lmio
 * @Date: 2023-03-23 16:24:27
 * @LastEditTime: 2023-04-07 14:37:18
 * @FilePath: /leetcode/code/72.go
 * @Description:72.编辑距离
 */
package code

import "leetcode/utils"

func MinDistance(word1 string, word2 string) int {
	l1, l2 := len(word1), len(word2)
	dp := make([][]int, l1+1);
	for i := range dp {
		dp[i] = make([]int, l2+1)
	}
	// dp数组初始化
	for j := 0; j <= l2; j++ {
		dp[0][j] = j
	}
	for i := 0; i <= l1; i++ {
		dp[i][0] = i
	}
	
	for i := 1; i <= l1; i++ {
		for j := 1; j <= l2; j++ {
			if word1[i-1] == word2[j-1] {
				//什么都不用做
				dp[i][j] = dp[i-1][j-1]
			}else {
				//选取增删改中步数最少的
				dp[i][j] = utils.Min(
					dp[i-1][j],
					dp[i][j-1],
					dp[i-1][j-1],
				) + 1
			}
		}
	}
	return dp[l1][l2]
}