/*
 * @Author: lmio
 * @Date: 2023-04-16 13:33:55
 * @LastEditTime: 2023-04-16 14:24:58
 * @FilePath: /leetcode/offer/67.go
 * @Description:面试题67. 把字符串转换成整数
 */
package offer

import (
	"leetcode/utils"
	"math"
)

func StrToInt(str string) int {
	var sign int
	isDight := func(bt byte) bool {
		if bt < '0' || bt > '9' {
			return false
		}
		return true
	}
	index := 0
	for index < len(str) && str[index] == ' ' {
		index++
	}
	switch str[index] {
		case '0', '1', '2', '3', '4', '5', '6', '7', '8', '9':
			sign = 1
		case '+':
			sign = 1
			index++
		case '-':
			sign = -1
			index++
		default:
			return 0
	}
	res := 0
	for index < len(str) && isDight(str[index]) {
		
		res *= 10
		res += int(str[index] - '0')
		if res > 2147483647 {
			if sign == 1{
				return math.MaxInt32
			}else {
				return math.MinInt32
			}
		}
		index++
	}
	return utils.Max(utils.Min(sign * res, 2147483647), -2147483648)
}