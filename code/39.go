/*
 * @Author: lmio
 * @Date: 2023-04-01 16:09:55
 * @LastEditTime: 2023-04-01 19:05:09
 * @FilePath: /leetcode/code/39.go
 * @Description:39.组合总和
 */
package code

import "sort"

func CombinationSum(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	res := [][]int{}
	ans := []int{}
	sum := 0
	var backbrack func(n int)
	backbrack = func(n int) {
		if sum > target {
			return
		}
		if sum == target {
			res = append(res, append([]int{}, ans...))
			return
		}
		for i := n; i < len(candidates); i++ {
			if sum + candidates[i] > target {
				break
			}
			ans = append(ans, candidates[i])
			sum += candidates[i]
			backbrack(i)
			ans = ans[:len(ans)-1]
			sum -= candidates[i]
		}
	}
	backbrack(0)
	return res
}