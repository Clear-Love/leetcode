/*
 * @Author: lmio
 * @Date: 2023-03-29 10:32:28
 * @LastEditTime: 2023-03-29 20:14:21
 * @FilePath: /leetcode/code/1091.go
 * @Description:1091. 二进制矩阵中的最短路径
 */
package code

/**
 * @description: 使用Bfs（查找最短路径时bfs效率通常较高，bfs常用队列实现，dfs常用递归，在用dfs实现时超时了）
 * @param {[][]int} grid
 * @return {*}
 */
func ShortestPathBinaryMatrix(grid [][]int) int {
	n, m := len(grid), len(grid[0])
	if grid[0][0] == 1 || grid[n-1][m-1] == 1 {
		return -1
	}

	visited := make([][]int, n)
	for i := range visited {
		visited[i] = make([]int, m)
	}
	visited[0][0] = 1
	move := [][]int{{0, 1}, {0, -1}, {1, 1}, {-1, -1}, {1, 0}, {-1, 0}, {-1, 1}, {1, -1}}
	
	type Node struct {
        X int
        Y int
        Step int
    }
	nodes := []*Node{{0, 0, 1}}

	for len(nodes) != 0 {
		node := nodes[0]
		nodes = nodes[1:]
		for _, d := range move {
			x, y := node.X + d[0], node.Y + d[1]
			if x >= 0 && y >= 0 && x < n && y < m && grid[x][y] == 0 && visited[x][y] == 0 {
				visited[x][y] = node.Step+1
				nodes = append(nodes, &Node{x, y, node.Step+1})
			}
		}
	}
    if visited[n-1][m-1] == 0 {
        return -1
    }
	return visited[n-1][m-1]
}