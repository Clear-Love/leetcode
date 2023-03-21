/*
 * @Author: lmio
 * @Date: 2023-02-07 22:48:18
 * @LastEditTime: 2023-02-19 23:35:20
 * @FilePath: /leetcode/code/695.go
 * @Description:695.岛屿的最大面积
 */
package code

import (
	"leetcode/template"
)


var (
	dx = []int{0, 1, 0, -1}
	dy = []int{1, 0, -1, 0}
)

func MaxAreaOfIsland(grid [][]int) int {
	max := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			max = template.Max(max, dfs(grid, i, j))
		}
	}
	return max
}

func dfs(grid [][]int, x, y int) int {
	if grid[x][y] == 1 {
		n, m := len(grid), len(grid[0])
		area := 1
		grid[x][y] = 0
		for i := 0; i < 4; i++ {
			_x, _y := x+dx[i], y+dy[i]
			if _x >= 0 && _x < n && _y >= 0 && _y < m {
				area += dfs(grid, _x, _y)
			}
		}
		return area
	}
	return 0
}