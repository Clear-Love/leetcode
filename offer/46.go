/*
 * @Author: lmio
 * @Date: 2023-04-01 13:35:01
 * @LastEditTime: 2023-04-01 14:22:35
 * @FilePath: /leetcode/offer/46.go
 * @Description:剑指 Offer 46. 把数字翻译成字符串
 */
package offer

import "strconv"

func TranslateNum(num int) int {
	str := strconv.Itoa(num)
	if len(str) == 1 {
		return 1
	}
	dp := make([]int, len(str))
	dp[0] = 1
	if str[0] > '0' && str[0] < '2' || str[0] == '2' && str[1] < '6' {
		dp[1] = 2
	}else {
		dp[1] = 1
	}
	for i := 2; i < len(dp); i++ {
		last := str[i-1]
		if last > '0' && last < '2' || last == '2' && str[i] < '6' {
			dp[i] = dp[i-1] + dp[i-2]
		}else {
			dp[i] = dp[i-1]
		}
	}
	return dp[len(str)-1]
}