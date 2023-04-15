/*
 * @Author: lmio
 * @Date: 2023-04-15 16:13:25
 * @LastEditTime: 2023-04-15 16:40:06
 * @FilePath: /leetcode/code/1042.go
 * @Description:1042. 不邻接植花
 */
package code

func GardenNoAdj(n int, paths [][]int) []int {
	// 创建邻接表
	graph := make([][]int, n)
	for _, path := range paths {
		u, v := path[0]-1, path[1]-1 // 节点编号从0开始，需要将输入的节点编号减1
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}

	// 创建结果数组，并初始化为0，表示尚未选择花种
	answer := make([]int, n)

	// 遍历每个花园
	for i := 0; i < n; i++ {
		used := [5]bool{} // 记录相邻花园中已使用的花种

		// 遍历相邻的花园
		for _, j := range graph[i] {
			used[answer[j]] = true
		}

		// 在未使用的花种中选择一种种植
		for k := 1; k <= 4; k++ {
			if !used[k] {
				answer[i] = k
				break
			}
		}
	}

	return answer
}