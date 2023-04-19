/*
 * @Author: lmio
 * @Date: 2023-04-19 20:35:01
 * @LastEditTime: 2023-04-19 21:33:14
 * @FilePath: /leetcode/offer/44.go
 * @Description:剑指 Offer 44. 数字序列中某一位的数字
 */
package offer

import (
	"leetcode/utils"
)

func FindNthDight(n int) int {
	preindex := 0
	index := 0
	dight := 1
	level := 1
	for n > index {
		preindex = index
		index += 9*dight*level
		dight *= 10
		level++
	}
	// 向上取整
	num := dight/10 + (n - preindex + level-2)/(level-1)-1
	i := (n - preindex)%(level-1)
	if i == 0 {
		return utils.GetNthDight(num, 0)
	}
	return utils.GetNthDight(num, level-i-1)
}