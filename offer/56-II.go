/*
 * @Author: lmio
 * @Date: 2023-04-12 10:23:38
 * @LastEditTime: 2023-04-12 10:39:04
 * @FilePath: /leetcode/offer/56-II.go
 * @Description:剑指 Offer 56 - II. 数组中数字出现的次数 II
 */
package offer

func SingleNumber(nums []int) int {
	dict := map[int]int{}
	for _, v := range nums {
		dict[v]++
		if dict[v] == 3 {
			delete(dict, v)
		}
	}
	var res int
	for k := range dict {
		res = k
	}
	return res
}