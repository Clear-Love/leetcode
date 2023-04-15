/*
 * @Author: lmio
 * @Date: 2023-04-15 13:21:48
 * @LastEditTime: 2023-04-15 13:54:30
 * @FilePath: /leetcode/offer/62.go
 * @Description:剑指 Offer 62. 圆圈中最后剩下的数字
 */
package offer

func LastRemaining(n, m int) int {
	var fn func(int) int
	fn = func(k int) int {
		if k == 1 {
			return 0
		}
		x := fn(k-1)
		return (m + x) % n
	}
	return fn(n)
}