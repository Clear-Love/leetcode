/*
 * @Author: lmio
 * @Date: 2023-03-29 10:11:49
 * @LastEditTime: 2023-03-29 10:29:39
 * @FilePath: /leetcode/offer/63.go
 * @Description:剑指 Offer 63. 股票的最大利润
 */
package offer

import (
	"leetcode/template"
	"math"
)

func MaxProfit(prices []int) int {
	cost := math.MaxInt
	profit := math.MinInt
	for _, price := range prices {
		cost = template.Min(cost, price)
		profit = template.Max(profit, price - cost)
	}
	return profit
}