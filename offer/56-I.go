/*
 * @Author: lmio
 * @Date: 2023-04-12 09:51:01
 * @LastEditTime: 2023-04-12 10:22:10
 * @FilePath: /leetcode/offer/56-I.go
 * @Description:剑指 Offer 56 - I. 数组中数字出现的次数
 */
package offer

func SingleNumbers(nums []int) []int {
	x, y, num := 0, 0, 0
	for _, v := range nums {
		num ^= v
	}
	m := 1
	// 找到倒数第一位为1的位
	for m & num == 0 {
		m = m << 1
	}
	for _, v := range nums {
		if v & m == 0 {
			x ^= v
		}else {
			y ^= v
		}
	}
	return []int{x, y}
}