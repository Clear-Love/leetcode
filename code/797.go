/*
 * @Author: lmio
 * @Date: 2023-03-29 21:50:13
 * @LastEditTime: 2023-03-29 22:36:26
 * @FilePath: /leetcode/code/797.go
 * @Description:797. 所有可能的路径
 */
package code

func AllPathsSourceTarget(graph [][]int) [][]int {
	n := len(graph)
	res := [][]int{}
	var dfs func(k int)
	visited := make([]bool, n)
	ans := []int{}
	dfs = func (k int) {
		ans = append(ans, k)
		if k == n-1 {
			res = append(res, append([]int{}, ans...))
			ans = ans[:len(ans)-1]
			return
		}
		visited[k] = true
		for _, i := range graph[k] {
			if !visited[i] {
				dfs(i)
			}
		}
		ans = ans[:len(ans)-1]
		visited[k] = false
	}
	dfs(0)
	return res
}