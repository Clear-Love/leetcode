/*
 * @Author: lmio
 * @Date: 2023-03-29 09:55:23
 * @LastEditTime: 2023-03-29 10:06:12
 * @FilePath: /leetcode/offer/10-I.go
 * @Description:剑指 Offer 10- I. 斐波那契数列
 */
package offer

func Fib(n int) int {
	var mod int = 1e9 + 7
	prev2, prev1, res := 0, 1, 1
	if n < 2 {
		return n
	}
	for i := 2; i <= n; i++ {
		res = (prev1 + prev2) % mod
		prev2 = prev1
		prev1 = res
	}
	return res
}