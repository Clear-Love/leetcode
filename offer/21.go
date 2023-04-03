/*
 * @Author: lmio
 * @Date: 2023-04-03 09:48:10
 * @LastEditTime: 2023-04-03 09:51:59
 * @FilePath: /leetcode/offer/21.go
 * @Description:剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
 */
package offer

func Exchange(nums []int) []int {
	odds := []int{}
	evens := []int{}
	for _, v := range nums {
		if v & 1 == 0 {
			evens = append(evens, v)
		}else {
			odds = append(odds, v)
		}
	}
	return append(odds, evens...)
}