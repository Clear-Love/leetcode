/*
 * @Author: lmio
 * @Date: 2023-04-04 10:00:16
 * @LastEditTime: 2023-04-04 10:23:16
 * @FilePath: /leetcode/code/413.go
 * @Description:413. 等差数列划分
 */
package code

func NumberOfArithmeticSlices(nums []int) int {
	type ariSlice struct {
		Div int
		Size int
	}
	n := len(nums)
	if n < 3 {
		return 0
	}
	dp := make([]ariSlice, n)
	// 防止第一位和第二位相等
	dp[0].Div = nums[1] - nums[0] + 1
	res := 0
	for i := 1; i < n; i++ {
		if nums[i] - nums[i-1] == dp[i-1].Div {
			dp[i].Size = dp[i-1].Size+1
			dp[i].Div = dp[i-1].Div
			res += dp[i].Size-2
		}else {
			dp[i].Div = nums[i] - nums[i-1]
			dp[i].Size = 2
		}
	}
	return res
}