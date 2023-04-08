/*
 * @Author: lmio
 * @Date: 2023-04-08 12:11:15
 * @LastEditTime: 2023-04-08 14:48:20
 * @FilePath: /leetcode/code/322.go
 * @Description:322. 零钱兑换
 */
package code

import (
	"leetcode/utils"
	"sort"
)

func CoinChange(coins []int, amount int) int {
	sort.Ints(coins)
	dp := make([]int, amount+1)
	for i := 1; i < len(dp); i++{
		dp[i] = amount+1
		for j := 0; j < len(coins); j++ {
			if i - coins[j] < 0 {
				break
			}
			dp[i] = utils.Min(dp[i-coins[j]]+1, dp[i])
		}
	}
	if dp[amount] == amount+1 {
		return -1
	}
	return dp[amount]
}