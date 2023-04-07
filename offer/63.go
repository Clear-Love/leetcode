/*
 * @Author: lmio
 * @Date: 2023-03-29 10:11:49
 * @LastEditTime: 2023-04-07 14:32:50
 * @FilePath: /leetcode/offer/63.go
 * @Description:剑指 Offer 63. 股票的最大利润
 */
package offer

import (
	"leetcode/utils"
	"math"
)

func MaxProfit(prices []int) int {
	cost := math.MaxInt
	profit := math.MinInt
	for _, price := range prices {
		cost = utils.Min(cost, price)
		profit = utils.Max(profit, price - cost)
	}
	return profit
}