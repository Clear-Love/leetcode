/*
 * @Author: lmio
 * @Date: 2023-02-22 20:45:47
 * @LastEditTime: 2023-02-22 21:05:54
 * @FilePath: /leetcode/code/200.go
 * @Description:200.岛屿的数量
 */
package code

func NumIsland(grid [][]byte) int {
	n, m := len(grid), len(grid[0])
	res := 0
	dx := []int{1, 0, -1, 0}
	dy := []int{0, 1, 0, -1}
	var clearIand func (x, y int)

	clearIand = func (x, y int) {
		if x < 0 || x >= n || y < 0 || y >= m || grid[x][y] != '1'{
			return
		}
		grid[x][y] = 0
		for i := 0; i < 4; i++ {
			_x := x + dx[i]
			_y := y + dy[i]
			clearIand(_x, _y)
		}
	}
	
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if grid[i][j] == '1' {
				res++
				clearIand(i, j)
			}
		}
	}
	return res
}