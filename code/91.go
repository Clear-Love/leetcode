/*
 * @Author: lmio
 * @Date: 2023-04-05 18:04:49
 * @LastEditTime: 2023-04-05 19:20:49
 * @FilePath: /leetcode/code/91.go
 * @Description:91. 解码方法
 */
package code

func NumDecodings(s string) int {
	if s[0] == '0' {
		return 0
	}
	if len(s) == 1 {
		return 1
	}
	dp := make([]int, len(s))
	dp[0] = 1
	if s[0] == '1' || s[0] == '2' &&  s[1] < '7' {
		dp[1] = 1 
	}
	if s[1] != '0' {
		dp[1] += 1
	}
	for i := 2; i < len(dp); i++ {
		last := s[i-1]
		if last == '1' || last == '2' &&  s[i] < '7' {
			dp[i] += dp[i-2]
		}
		if s[i] != '0' {
			dp[i] += dp[i-1]
		}
	}
	return dp[len(s)-1]
}