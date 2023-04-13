/*
 * @Author: lmio
 * @Date: 2023-04-13 08:13:36
 * @LastEditTime: 2023-04-13 08:19:57
 * @FilePath: /leetcode/offer/66.go
 * @Description:剑指 Offer 66. 构建乘积数组
 */
package offer

func ConstructArr(a []int) []int {
	res := make([]int, len(a))
	sum := 1
	for i := range a {
		res[i] = sum
		sum *= a[i]
	}
	sum = 1
	for i := len(a)-1; i >= 0; i-- {
		res[i] *= sum
		sum *= a[i]
	}
	return res
}