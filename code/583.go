/*
 * @Author: lmio
 * @Date: 2023-04-07 15:21:28
 * @LastEditTime: 2023-04-07 15:40:14
 * @FilePath: /leetcode/code/583.go
 * @Description:583. 两个字符串的删除操作
 */
package code

import "leetcode/utils"

/**
 * @description: 每步 可以删除任意一个字符串中的一个字符。
 * @param {string} word1 单词 只包含小写英文字母
 * @param {string} word2 单词 只包含小写英文字母
 * @return {*} 返回使得 word1 和  word2 相同所需的最小步数
 */
func MinDistance_(word1 string, word2 string) int {
	n, m := len(word1)+1, len(word2)+1
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, m)
	}
	for i := 0; i < n; i++ {
		dp[i][0] = i
	}
	for i := 0; i < m; i++ {
		dp[0][i] = i
	}
	for i := 1; i < n; i++ {
		for j := 1; j < m; j++ {
			if word1[i-1] == word2[j-1] {
				dp[i][j] = dp[i-1][j-1]
			}else {
				dp[i][j] = utils.Min(dp[i][j-1], dp[i-1][j])+1
			}
		}
	}
	return dp[n-1][m-1]
}