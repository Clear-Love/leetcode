/*
 * @Author: lmio
 * @Date: 2023-04-19 21:05:55
 * @LastEditTime: 2023-04-19 21:08:18
 * @FilePath: /leetcode/utils/number.go
 * @Description:
 */
package utils

/**
 * @description: 返回一个整数的第n位
 * @param {int} num
 * @param {int} n
 * @return {*}
 */
func GetNthDight(num int, n int) int {
	if n < 0 {
		num = -num
	}
	for i := 0; i <= n; i++ {
		if i == n {
			return num%10
		}
		num /= 10
		if num == 0{
			return -1
		}
	}
	return -1
}