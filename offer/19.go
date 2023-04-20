/*
 * @Author: lmio
 * @Date: 2023-04-19 21:38:57
 * @LastEditTime: 2023-04-19 23:37:20
 * @FilePath: /leetcode/offer/19.go
 * @Description:剑指 Offer 19. 正则表达式匹配
 */
package offer

func IsMatch(s string, p string) bool {
	ls, lp := len(s)+1, len(p)+1
	dp := make([][]bool, ls)
	for i := range dp {
		dp[i] = make([]bool, lp)
	}
	dp[0][0] = true
	for j := 2; j < lp; j++ {
		// 若*匹配0次
		dp[0][j] = p[j-1] == '*' && dp[0][j-2]
	}
	for i := 1; i < ls; i++ {
		for j := 1; j < lp; j++ {
			if p[j-1] == '*' {
				dp[i][j] =dp[i][j-2]
				if s[i-1] == p[j-2] || p[j-2] == '.' {
					dp[i][j] = dp[i][j] || dp[i-1][j]
				}
			}else if p[j-1] == '.' || s[i-1] == p[j-1] {
				dp[i][j] = dp[i-1][j-1]
			}
		}
	}
	return dp[ls-1][lp-1]
}