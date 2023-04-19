/*
 * @Author: lmio
 * @Date: 2023-04-19 15:55:07
 * @LastEditTime: 2023-04-19 20:34:13
 * @FilePath: /leetcode/offer/43.go
 * @Description:剑指 Offer 43. 1～n 整数中 1 出现的次数
 */
package offer

func CountDigitone(n int) int {
	dight := 1
	res := 0
	high, cur, low := n/10, n%10, 0
	for high != 0 || cur != 0 {
		if cur == 0 {
			res += high*dight
		}else if cur == 1 {
			res += high*dight+low+1
		}else {
			res += (high+1)*dight
		}
		low += cur*dight
		cur = high%10
		dight *= 10
		high /= 10
	}
	return res
}