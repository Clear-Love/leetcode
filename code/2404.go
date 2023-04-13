/*
 * @Author: lmio
 * @Date: 2023-04-13 08:21:28
 * @LastEditTime: 2023-04-13 08:27:27
 * @FilePath: /leetcode/code/2404.go
 * @Description:2404. 出现最频繁的偶数元素
 */
package code

import "leetcode/utils"

func MostFrequentEven(nums []int) int {
	min := -1
	count := 0
	m := map[int]int{}
	for _, v := range nums {
		if v & 1 == 1 {
			continue
		}
		m[v]++
		if m[v] == count {
			min = utils.Min(min, v)
			count = m[v]
		}else if m[v] > count {
			min = v
			count = m[v]
		}
	}
	return min	
}