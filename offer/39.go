/*
 * @Author: lmio
 * @Date: 2023-04-13 08:07:52
 * @LastEditTime: 2023-04-13 08:12:19
 * @FilePath: /leetcode/offer/39.go
 * @Description:剑指 Offer 39. 数组中出现次数超过一半的数字
 */
package offer

func MajorityElement(nums []int) int {
	max := 0
	count := 0
	m := map[int]int{}
	for _, v := range nums {
		m[v]++
		if m[v] > count {
			count = m[v]
			max = v
		}
	}
	return max
}