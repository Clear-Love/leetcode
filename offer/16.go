/*
 * @Author: lmio
 * @Date: 2023-04-10 08:18:09
 * @LastEditTime: 2023-04-10 08:23:31
 * @FilePath: /leetcode/offer/16.go
 * @Description:剑指 Offer 16. 数值的整数次方
 */
package offer

func MyPow(x float64, n int) float64 {
	res := 1.0
	if n < 0 {
		x = 1.0/x
	}
	for n > 0 {
		if n & 1 == 1 {
			res *= x
		}
		x *= x
		n = n >> 1
	}
	return res
}