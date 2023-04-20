/*
 * @Author: lmio
 * @Date: 2023-04-20 09:16:01
 * @LastEditTime: 2023-04-20 15:31:22
 * @FilePath: /leetcode/offer/60.go
 * @Description:剑指 Offer 60. n个骰子的点数
 */
package offer

func DicesProbability(n int) []float64 {
	dp := make([]float64, 6)
	for i := range dp {
		dp[i] = 1.0/6
	}
	// i 骰子个数 dp[j] i-1个骰子点数和为j的概率
	// k 当前骰子掷出的点数-1
	for i := 2; i <= n; i++ {
		temp := make([]float64, 5*i+1)
		for j := 0; j < len(dp); j++ {
			for k := 0; k < 6; k++ {
				temp[j + k] += dp[j]/6.0
			}
		}
		dp = temp
	}
	return dp
}