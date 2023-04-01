/*
 * @Author: lmio
 * @Date: 2023-04-01 15:07:51
 * @LastEditTime: 2023-04-01 16:08:57
 * @FilePath: /leetcode/code/47.go
 * @Description:47. 全排列 II
 */
package code

import "sort"

func PermuteUnique(nums []int) [][]int {
	sort.Ints(nums)
	res := [][]int{}
	ans := make([]int, 0, len(nums))
	visited := make([]bool, len(nums))
	var backbrack func(n int)
	backbrack = func(n int) {
		if n == len(nums) {
			res = append(res, append([]int{}, ans...))
			return
		}
		for i := 0; i < len(nums); i++ {
			if visited[i] || i > 0 && nums[i] == nums[i-1] && !visited[i-1] {
				continue
			}
			ans = append(ans, nums[i])
			visited[i] = true
			backbrack(n+1)
			ans = ans[:len(ans)-1]
			visited[i] = false
		}
	}
	backbrack(0)
	return res
}