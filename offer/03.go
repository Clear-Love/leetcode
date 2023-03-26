/*
 * @Author: lmio
 * @Date: 2023-03-26 21:18:32
 * @LastEditTime: 2023-03-26 21:23:12
 * @FilePath: /leetcode/offer/03.go
 * @Description:剑指 Offer 03. 数组中重复的数字
 */
package offer

func FindRepeatNumber(nums []int) int {
	apper := make([]int, len(nums))
	for _, v := range nums {
		if apper[v] == 1 {
			return v
		}
		apper[v] = 1;
	}
	return -1
}