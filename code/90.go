/*
 * @Author: lmio
 * @Date: 2023-03-30 10:18:40
 * @LastEditTime: 2023-03-30 10:25:36
 * @FilePath: /leetcode/code/90.go
 * @Description:90.子集
 */
package code

import "sort"

func SubsetsWithDup(nums []int) [][]int {
	sort.Ints(nums)
	res := [][]int{}
	ans := []int{}
	used := make([]bool, len(nums))
	var backbrack func(l, k int)
	backbrack = func (l, k int) {
		if len(ans) == l {
			res = append(res, append([]int{}, ans...))
			return
		}
		for i := k; i < len(nums); i++ {
			if i > 0 && nums[i] == nums[i-1] && !used[i-1] {
				continue
			}
			ans = append(ans, nums[i])
			used[i] = true
			backbrack(l, i+1)
			ans = ans[:len(ans)-1]
			used[i] = false
		}
	}
	for i := 0; i <= len(nums); i++ {
		backbrack(i, 0)
	}
	return res
}