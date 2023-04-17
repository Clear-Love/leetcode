/*
 * @Author: lmio
 * @Date: 2023-04-17 16:11:57
 * @LastEditTime: 2023-04-17 16:18:42
 * @FilePath: /leetcode/offer/17.go
 * @Description:剑指 Offer 17. 打印从1到最大的n位数
 */
package offer

import "math"

func PrintNumbers(n int) []int {
	max := int(math.Pow10(n))
	res := make([]int, max-1)
	for i := range res {
		res[i] = i+1
	}
	return res
}