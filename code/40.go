/*
 * @Author: lmio
 * @Date: 2023-04-01 17:57:08
 * @LastEditTime: 2023-04-01 19:03:49
 * @FilePath: /leetcode/code/40.go
 * @Description:40. 组合总和 II
 */
package code

import "sort"

func CombinationSum2(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	res := [][]int{}
	ans := []int{}
	visited := make([]bool, len(candidates))
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
			if i > 0 && candidates[i] == candidates[i-1] && !visited[i-1] {
				continue
			}
			ans = append(ans, candidates[i])
			sum += candidates[i]
			visited[i] = true
			backbrack(i+1)
			ans = ans[:len(ans)-1]
			visited[i] = false
			sum -= candidates[i]
		}
	}
	backbrack(0)
	return res
}