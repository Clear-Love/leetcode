/*
 * @Author: lmio
 * @Date: 2023-03-23 22:22:00
 * @LastEditTime: 2023-03-23 22:55:55
 * @FilePath: /leetcode/code/50.go
 * @Description:50.Pow(x, n)
 */
package code

func MyPow(x float64, n int) float64 {
	var ans float64 = 1
	if n < 0 {
		x, n = 1/x, -n
	}
	for n > 0 {
		// 奇数
		if(n&1 == 1) {
			ans *= x
		}
		x *= x
		n = n >> 1
	}
	return ans
} 