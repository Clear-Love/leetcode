/*
 * @Author: lmio
 * @Date: 2023-04-04 09:08:27
 * @LastEditTime: 2023-04-04 09:55:52
 * @FilePath: /leetcode/code/5.go
 * @Description:5.最长回文子串
 */
package code

func LongestPalindrome(s string) string {
	n := len(s)
	dp := make([][]bool, n)
	for i := range dp {
		dp[i] = make([]bool, n)
	}
	start := 0
	long := 0
	for j := 0; j < n; j++ {
		for i := n-j-1; i + j < n && i >= 0; i-- {
			if s[i] != s[i+j] {
				continue
			}
			if j < 2 || j >= 2 && dp[i+1][i+j-1]{
				dp[i][i+j] = true
				if j > long {
					start = i
					long = j
				}
			}
		}
	}
	return s[start:start+long+1]
}