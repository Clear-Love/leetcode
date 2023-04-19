/*
 * @Author: lmio
 * @Date: 2023-04-17 21:28:56
 * @LastEditTime: 2023-04-18 10:22:24
 * @FilePath: /leetcode/offer/14-II.go
 * @Description:剑指 Offer 14- II. 剪绳子 II
 */
package offer

import "leetcode/utils"

func CuttingRopeII(n int) int {
	if n <= 3 {
		return n-1
	}
	p := 1000000007
	a := n / 3
	b := n % 3
	if b == 0 {
		return utils.Remainder(3, a, p)
	}else if b == 1 {
		return (utils.Remainder(3, a-1, p)*4)%p
	}else {
		return (utils.Remainder(3, a, p)*2)%p
	}
}