/*
 * @Author: lmio
 * @Date: 2023-04-06 09:20:39
 * @LastEditTime: 2023-04-06 09:33:12
 * @FilePath: /leetcode/offer/61.go
 * @Description:面试题61. 扑克牌中的顺子
 */
package offer

import "sort"

func IsStraight(nums []int) bool {
	sort.Ints(nums)
	skipCont := 0
	if nums[0] == 0 {
		skipCont++
	}
	for i := 1; i < len(nums); i++ {
		if nums[i] == 0 {
			skipCont++
			continue
		}
		var div int
		if nums[i-1] != 0 {
			div = nums[i] - nums[i-1]
		}else {
			div = 1
		}
		
		if div > 1 && skipCont >= div-1 {
			skipCont -= div -1
			continue
		}
		if div != 1 {
			return false
		}
	}
	return true
}